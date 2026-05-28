from httpx import Response

from clients.api_client import ApiClient
import allure

from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class BannersClient(ApiClient):
    """класс работы с апи api/Banners"""
    @allure.step("Get banners")
    def get_banners(self) -> Response:
        """получение списка баннеров"""
        return self.get("/api/Banners/getBanners")






#Клиент для работы с баннерами
def get_banners_client(user : AuthenticationUserSchema) -> BannersClient:
    """Создаем приватный клиент работы с апи баннеров"""
    return BannersClient(client=get_private_http_client_no_cert(user))