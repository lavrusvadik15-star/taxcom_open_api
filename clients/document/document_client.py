from xml.dom.minidom import Document

import allure
import httpx
from httpx import Response

from clients.api_client import ApiClient
from clients.document.document_schema import CreateDocumentRequestSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class DocumentClient(ApiClient):
    """Класс работы с созданием документов"""

    @allure.step("Create Nonformalized")
    def create_nonformalized_document(self, request:CreateDocumentRequestSchema) -> Response:
        """Создание НФД"""
        return self.post("/api/Document/createNonformalized", json= request.model_dump(by_alias=True))





#Делаем клиент для работы с апи
def get_document_client(user: AuthenticationUserSchema) -> DocumentClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return DocumentClient(client=get_private_http_client_no_cert(user))

#Клиент для работы с закрытым апи авторизации по сертификату
def get_document_cert_client(http_client: httpx.Client) -> DocumentClient:
    """Создаем клиент на основе авторизации по сертификату"""
    return DocumentClient(client=http_client)
