import allure
from httpx import Response

from clients.api_client import ApiClient
from clients.department.department_schema import CreateDepartmentRequestSchema, UpdateDepartmentRequestSchema, \
    DeleteDepartmentRequestSchema
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

    @allure.step('Create new department')
    def create_new_department(self, request: CreateDepartmentRequestSchema) -> Response:
        """Создание нового департамента"""
        return self.post("/api/Department/add", json= request.model_dump(by_alias=True))

    @allure.step('Update department')
    def update_department(self, request: UpdateDepartmentRequestSchema) -> Response:
        """Обновление данных о депортаменте"""
        return self.post("/api/Department/update", json= request.model_dump(by_alias=True))

    def delete_department(self, request: DeleteDepartmentRequestSchema) -> Response:
        """Удаление подраздления"""
        return self.delete("/api/Department/delete", json= request.model_dump(by_alias=True))







#Делаем клиент для работы с апи
def get_department_client(user: AuthenticationUserSchema) -> DepartmentClient:
    """Создаем клиента по переданному пользователю в создании приватного клиента"""
    return DepartmentClient(client=get_private_http_client_no_cert(user))