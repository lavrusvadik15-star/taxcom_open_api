import allure
from httpx import Response

from clients.abonent.abonent_client import AbonentClient
from clients.api_client import ApiClient
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class AdvisersClient(ApiClient):
    """
    Класс для работы с api/Advisers
    """
    @allure.step("Получение списка адвайзеров")
    def get_advisers(self) -> Response:
        """
        Метод получения всех доступных Адвайнер
        :return:
        """
        return self.get("api/Advisers/getAdvisers")







#Делаем клиент для работыс адвайзерами
def get_advisers_client(user : AuthenticationUserSchema) -> AdvisersClient:
    """
    Функция создания клиента для работы с адвайзером без серта
    :param user:
    :return:
    """
    return AdvisersClient(client=get_private_http_client_no_cert(user))