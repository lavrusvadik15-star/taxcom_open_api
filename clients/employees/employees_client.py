import allure
import httpx
from httpx import Response

from clients.api_client import ApiClient
from clients.employees.employees_schema import CreateEmployeeRequestSchema, UpdateEmployeeRequestSchema, \
    GetEmployeeRequestSchema, DeleteEmployeeRequestSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert


class EmployeesClient(ApiClient):
    """Класс для работы с API сотрудников"""

    @allure.step("Получение списка всех пользователей")
    def get_list_employees(self) -> Response:
        """Метод получения списка сотрудников"""
        return self.get("api/Employees/listEmployees")

    @allure.step("Создание пользователя")
    def create_employee(self, request: CreateEmployeeRequestSchema) -> Response:
        """ Метод создания нового работника """
        return self.post("api/Employees/add", json= request.model_dump(by_alias=True))

    @allure.step("Изменить данные о пользователе")
    def update_employee(self, request: UpdateEmployeeRequestSchema) -> Response:
        """Метод изменения данных у существующего пользователя"""
        return self.post("api/Employees/update", json= request.model_dump(by_alias=True))

    @allure.step("Получить детальные данные по сотруднику")
    def get_employee(self, query: GetEmployeeRequestSchema) -> Response:
        """Метод получает подробные сведения об одном сотруднике"""
        return self.get("api/Employees/getEmployee", params=query.model_dump(by_alias=True))

    @allure.step("Удалить пользователя")
    def delete_employee(self, query: DeleteEmployeeRequestSchema):
        """Метод удаления сотрудника"""
        return self.get("api/Employees/delete", params=query.model_dump(by_alias=True))




#Создаем клиент
def get_employees_client(user: AuthenticationUserSchema) -> EmployeesClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return EmployeesClient(client=get_private_http_client_no_cert(user))

#Клиент по серту
def get_employees_cert_client(http_client: httpx.Client) -> EmployeesClient:
    """Создаем клиент на основе авторизации по сертификату"""
    return EmployeesClient(client=http_client)