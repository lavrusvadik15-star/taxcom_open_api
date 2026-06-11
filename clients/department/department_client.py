import allure
from httpx import Response

from clients.api_client import ApiClient
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class DepartmentClient(ApiClient):
    """ Класс для работы с апи api/Department/listAvailableDepartments"""

    @allure.step("Get list available departmens")
    def get_list_departments(self) -> Response:
        """Метод получения списка доступных отделов"""
        return self.get("/api/Department/listAvailableDepartments")

    @allure.step('Get tree departments')
    def get_tree_departments(self) -> Response:
        """Получение дерева подразделений"""
        return self.get("/api/Department/tree")







#Делаем клиент для работы с апи
def get_department_client(user: AuthenticationUserSchema) -> DepartmentClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return DepartmentClient(client=get_private_http_client_no_cert(user))