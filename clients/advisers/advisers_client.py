import allure
from httpx import Response

from clients.abonent.abonent_client import AbonentClient
from clients.advisers.advisers_schema import AdvisersSchema, SubscribeAdvisersRequestSchema, \
    UnsubscribeAdvisersRequestSchema
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

    @allure.step("Подписаться на адвайзер")
    def subscribe_adviser(self, request: SubscribeAdvisersRequestSchema) -> Response:
        """Метод подписки
        :param request:
        :return:
        """
        return self.post("/api/Advisers/subscribeAdviser", json=request.model_dump(by_alias=True))

    @allure.step("Отписаться от адвайзера")
    def unsubcribe_adviser(self, request: UnsubscribeAdvisersRequestSchema) -> Response:
        """Метод отписки от адвайзера
        :param request:
        :return:
        """
        return self.post("/api/Advisers/unSubscribeAdviser", json=request.model_dump(by_alias=True))

    @allure.step("Получить список подписанных адвазеров")
    def get_adviser_subscription(self) -> Response:
        """Метод получить все подисанные айдивизеры"""
        return self.get("/api/Advisers/getAdviserSubscription")






#Делаем клиент для работыс адвайзерами
def get_advisers_client(user : AuthenticationUserSchema) -> AdvisersClient:
    """
    Функция создания клиента для работы с адвайзером без серта
    :param user:
    :return:
    """
    return AdvisersClient(client=get_private_http_client_no_cert(user))