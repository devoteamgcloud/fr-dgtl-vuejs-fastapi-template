from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy import asc, desc
from sqlalchemy.orm import Query
from sqlmodel import Session, SQLModel

from app.models.base import Page, QueryFilter, TableBase, to_snake

ModelType = TypeVar("ModelType", bound=TableBase)
CreateModelType = TypeVar("CreateModelType", bound=SQLModel)
UpdateModelType = TypeVar("UpdateModelType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateModelType, UpdateModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLModel class
        """
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self,
        db: Session,
        *,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filters: Optional[List[QueryFilter]] = [],
        is_desc: bool = False,
    ) -> Page[ModelType]:
        q = db.query(self.model)
        if filters:
            q = self.update_query_with_filters_(q, filters)

        return self.order_and_paginate_results(
            q, skip=skip, limit=limit, sort=sort, is_desc=is_desc
        )

    def create(self, db: Session, *, obj_in: CreateModelType, commit: bool = True) -> ModelType:
        db_obj = self.model.from_orm(obj_in)
        db.add(db_obj)
        if commit:
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateModelType, Dict[str, Any]],
        commit: bool = True,
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            snake_field = to_snake(field)
            if snake_field in update_data:
                setattr(db_obj, snake_field, update_data[snake_field])

        db.add(db_obj)
        if commit:
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int, commit: bool = True) -> Optional[ModelType]:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        if commit:
            db.commit()
        return obj

    def order_and_paginate_results(
        self,
        q: Query,
        *,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        is_desc: bool = False,
    ) -> Page[ModelType]:
        if sort:
            sort = to_snake(sort)
            try:
                sort_field = getattr(self.model, sort)
                order_by = desc(sort_field) if is_desc else asc(sort_field)
                q = q.order_by(order_by)
            except AttributeError:
                pass

        if skip is not None:
            q = q.offset(skip)

        if limit is not None:
            q = q.limit(limit)

        total = q.count()
        items = q.all()

        return Page(items=items, total=total)

    def update_query_with_filters_(self, q: Query, query_filters: List[QueryFilter]) -> Query:
        operator_matcher = {
            "alchemy_func": {
                "=": "__eq__",
                "!=": "__ne__",
                ">": "__gt__",
                "<": "__lt__",
                ">=": "__ge__",
                "<=": "__le__",
                ":": "like",
                "in": "in_",
                "not_in": "notin_",
                "is_null": "is_",
                "is_not_null": "is_not",
            },
            "built_in": {
                "is_empty": '== ""',
                "is_not_empty": '!= ""',
                "is_true": "== True",
                "is_false": "== False",
            },
        }
        for query_filter in query_filters:
            q = self.manage_operators(q, query_filter, operator_matcher)

        return q

    def manage_operators(
        self, q: Query, query_filter: QueryFilter, operator_matcher: dict
    ) -> Query:
        attribute = getattr(self.model, query_filter.field)
        if not attribute:
            raise AttributeError(f"{self.model.__name__} has no attribute {query_filter.field}")
        if query_filter.operator in operator_matcher["alchemy_func"]:
            operator_value = operator_matcher["alchemy_func"][query_filter.operator]
            column_operator = getattr(attribute, operator_value)
            q = q.filter(column_operator(query_filter.value))
        elif query_filter.operator in operator_matcher["built_in"]:
            operator_value = operator_matcher["built_in"][query_filter.operator]
            q = q.filter(eval(f"{attribute} {operator_value}", {self.model.__name__: self.model}))
        else:
            raise ValueError(f"Operator {query_filter.operator} is not supported")

        return q