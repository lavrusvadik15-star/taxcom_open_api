from http import HTTPStatus

import pytest
import allure

from clients.employees.employees_client import EmployeesClient
from clients.employees.employees_schema import GetListEmployeesResponseSchema
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.employees import assert_get_list_employees
from tools.assertions.json import validate_json_schema


@pytest.mark.regression
@pytest.mark.employees
@allure.tag(AllureTags.EMPLOYEES, AllureTags.REGRESSION)
class TestEmployees:
    """Класс для тестирования сотрудников"""

    @allure.title("Get list employees")
    def test_get_list_employees(self, employees_client: EmployeesClient):
        response= employees_client.get_list_employees()
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetListEmployeesResponseSchema.model_validate_json(response.text)
        #Проверка данных в массиве (если они там есть)
        assert_get_list_employees(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_data.model_json_schema())

    @allure.title("Create new employee")
    def test_create_new_employee(self, employees_client: EmployeesClient):
        pass