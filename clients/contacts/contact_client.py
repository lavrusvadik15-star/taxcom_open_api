import allure
from httpx import Response

from clients.api_client import ApiClient


class ContactClient(ApiClient):
    """Класс для работы с апи контактов"""

    @allure.step("Get list of contacts")
    def get_contact_list(self) -> Response:
        """метод получения списка контактов"""
        return self.get("/")