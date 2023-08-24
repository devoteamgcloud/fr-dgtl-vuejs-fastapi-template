import json
from typing import Generator, List, NoReturn, Optional

import httpx
from fastapi import Depends, Header, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from google.auth import jwt
from sqlmodel import Session

from app import crud
from app.core.cloud_logging import log
from app.core.config import settings
from app.db.engine import engine
from app.models.base import QueryFilter
from app.models.user import User, UserCreate

oauth2_scheme = HTTPBearer()


def get_session() -> Generator:
    with Session(engine) as session:
        yield session


def get_current_user(
    db: Session = Depends(get_session),
    creds: HTTPAuthorizationCredentials = Security(oauth2_scheme),
) -> None:
    # TODO verify token and return claims
    pass


def get_iap_user(
    db: Session = Depends(get_session),
    x_goog_iap_jwt_assertion: Optional[str] = Header(None),
) -> User:

    email_to_check = None
    if settings.ENV in ["local", "test"]:
        email_to_check = settings.LOCAL_EMAIL_ADMIN
    else:
        if not x_goog_iap_jwt_assertion:
            log.info("No IAP JWT header")
            raise_401()

        if not settings.PROJECT_NUMBER or not settings.PROJECT_ID:
            log.info(
                "PROJECT_NUMBER and PROJECT_ID must be specified in order to verify JWT audience"
            )
            raise_500()

        # Verify JWT header
        jwt_header = jwt.decode_header(x_goog_iap_jwt_assertion)
        if "kid" not in jwt_header:
            log.info("Missing 'kid' value in JWT header")
            raise_401()

        url = "https://www.gstatic.com/iap/verify/public_key"
        public_key = httpx.get(url).json().get(jwt_header["kid"])

        # Decode JWT with public key
        # and verify content
        try:
            jwt_decoded = jwt.decode(x_goog_iap_jwt_assertion, certs=public_key)
            if jwt_decoded["iss"] != "https://cloud.google.com/iap":
                raise Exception("Wrong issuer")
            if (
                jwt_decoded["aud"]
                != "/projects/" + settings.PROJECT_NUMBER + "/apps/" + settings.PROJECT_ID
            ):
                raise Exception("Wrong audience")
        except Exception:
            log.exception("Invalid JWT")
            raise_401()

        email_to_check = jwt_decoded["email"]

    if email_to_check is None:
        log.info("Email from jwt is empty... This should not happend")
        raise_401()

    # Check that user from jwt exists in DB
    {% raw %}
    email_filter = parse_query_filter_params(
        f'{{"field": "email", "operator": "=", "value": "{email_to_check}"}}'
    )
    {% endraw %}
    
    user = crud.users.get_multi(db, filters=email_filter)
    if user.total == 0:
        # We assume that email has firstname.lastname@domain format
        # to fill firstname and lastname user's fields
        # This won't currenlty work for other format
        log.info((f"User {email_to_check} not found in DB. Creating user..."))
        splitted_email = email_to_check.split(".")
        first_name = splitted_email[0]
        last_name = splitted_email[1].split("@")[0]
        user_in = UserCreate(
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            email=email_to_check,
        )
        return crud.users.create(db=db, obj_in=user_in)

    return user.items[0]


def raise_401() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authorized.",
    )


def raise_403() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden.",
    )


def raise_500() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal Server Error",
    )


def parse_query_filter_params(filters: Optional[str] = None) -> List[QueryFilter]:
    if not filters:
        return []

    query_filters = json.loads(filters)

    if isinstance(query_filters, list):
        return [QueryFilter(**filter_) for filter_ in query_filters]
    elif isinstance(query_filters, dict):
        return [QueryFilter(**query_filters)]
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid filters",
        )
