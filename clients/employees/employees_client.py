import allure
from httpx import Response

from clients.api_client import ApiClient
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class EmployeesClient(ApiClient):
    """Класс для работы с API сотрудников"""

    @allure.step("Получение списка всех пользователей")
    def get_list_employees(self) -> Response:
        """Метод получения списка сотрудников"""
        return self.get("api/Employees/listEmployees")




#Создаем клиент
def get_employees_client(user: AuthenticationUserSchema) -> EmployeesClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return EmployeesClient(client=get_private_http_client_no_cert(user))