import json

import allure
import httpx
from httpx import Response

from clients.api_client import ApiClient
from clients.contacts.contact_schema import GetContactListRequestSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class ContactClient(ApiClient):
    """Класс для работы с апи контактов"""

    @allure.step("Get list of contacts")
    def get_contact_list(self, request: GetContactListRequestSchema) -> Response:
        """метод получения списка контактов"""
        return self.post("/api/Contacts/getContactList", json= request.model_dump(by_alias=True))

    @allure.step("Get Contact Invitations")
    def get_contact_invitations(self) -> Response:
        """Метод получения приглашений"""
        return self.post("/api/Contacts/getContactInvitations")

    @allure.step("Get Contact List As Dictionary Items")
    def get_contact_list_as_dictionary(self) -> Response:
        """Получение контактов в простом виде"""
        return self.get("/api/Contacts/getContactListAsDictionaryItems")








#Делаем клиент для работы с апи
def get_contacts_client(user: AuthenticationUserSchema) -> ContactClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return ContactClient(client=get_private_http_client_no_cert(user))

#Клиент для работы с закрытым апи авторизации по сертификату
def get_contacts_cert_client(http_client: httpx.Client) -> ContactClient:
    """Создаем клиент на основе авторизации по сертификату"""
    return ContactClient(client=http_client)