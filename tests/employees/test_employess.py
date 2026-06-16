import json
from http import HTTPStatus

import pytest
import allure
from httpx import request

from clients.employees.employees_client import EmployeesClient
from clients.employees.employees_schema import GetListEmployeesResponseSchema, CreateEmployeeRequestSchema, \
    EmployeeAuthoritySchema, CreateEmployeeResponseSchema
from fixtures.department import Department
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.employees import assert_get_list_employees, assert_create_new_employee
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
    def test_create_new_employee(self, employees_client: EmployeesClient, list_departments: Department):
        request = CreateEmployeeRequestSchema(department_id= list_departments.get_department_id)
        response = employees_client.create_employee(request)
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Т.к. в ответе просто приходится id нового департамента, то обернем его
        raw_data = json.loads(response.content)
        wrapped_data = {"id_new_employee": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

        response_data = CreateEmployeeResponseSchema.model_validate_json(json_wrapped)
        # Вадидация что там действительно новый ID
        assert_create_new_employee(response_data.id_new_employee)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(wrapped_data,response_data.model_json_schema())
        print(response_data)