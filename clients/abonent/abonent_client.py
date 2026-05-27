from httpx import Response

from clients.abonent.abonent_schema import GetAbonentRequest
from clients.api_client import ApiClient
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class AbonentClient(ApiClient):
    """
    Работа с /api/Abonent
    """
    def get_abonent(self, query: GetAbonentRequest) -> Response:
        """
        Получение данных абонента по AbonentId
        :param query:
        :return:
        """
        #params = {"AbonentId": query.Abonent_id}
        return self.get(f"/api/Abonent/getAbonent", params=query.model_dump(by_alias=True))

    def get_abonent_requisites(self, query: GetAbonentRequest) -> Response:
        """
        Получаем реквизиты по AbonentId
        :param query:
        :return:
        """
        return self.get(f"api/Abonent/getAbonentRequisites", params=query.model_dump(by_alias=True))

    def available_departments(self, query: GetAbonentRequest) -> Response:
        """
        Получает список доступных подразделений
        :param query:
        :return:
        """
        return self.get(f"/api/Abonent/availableDepartments", params=query.model_dump(by_alias=True))

    def get_mobile_qr(self ) -> Response:
        """Получения QR кода"""
        return self.get(f"api/Abonent/qr")

    def get_autopilot_status(self) -> Response:
        """Статус подключения ассистента - сдк"""
        return self.get(f"api/Abonent/autopilotStatus")



def get_abonent_client(user : AuthenticationUserSchema) -> AbonentClient:
    """
    Получить клиента для работы со abonent без серта
    :param user:
    :return:
    """
    return AbonentClient(client=get_private_http_client_no_cert(user))