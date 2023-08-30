import google.cloud.firestore as firestore

from app.core.cloud_logging import Singleton


class Firestore(metaclass=Singleton):
    def __init__(self) -> None:
        self.client = firestore.Client()

    def get_all_documents(self, collection_name: str, as_dict=True) -> list[dict]:
        doc_list = self.client.collection(collection_name).get()
        if not as_dict:
            return doc_list
        return [document.to_dict() for document in doc_list]

    def get_document(
        self, collection_name: str, document_id: str, as_dict=True
    ) -> firestore.DocumentReference | dict:
        doc = self.client.collection(collection_name).document(document_id).get()
        if not as_dict:
            return doc
        return doc.to_dict()

    def add_document(
        self, collection_name: str, data: dict
    ) -> firestore.DocumentReference:
        return self.client.collection(collection_name).add(data)

    def update_document(
        self, collection_name: str, document_id: str, data: dict
    ) -> firestore.DocumentReference:
        return (
            self.client.collection(collection_name).document(document_id).update(data)
        )

    def delete_document(self, collection_name: str, document_id: str):
        return self.client.collection(collection_name).document(document_id).delete()
