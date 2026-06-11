from http import HTTPStatus

import pytest
import allure

from clients.department import department_client
from clients.department.department_client import DepartmentClient
from clients.department.department_schema import GetListDepartmentsResponseSchema, GetDepartmentTreeResponseSchema, \
    CreateDepartmentRequestSchema
from fixtures.department import Department
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code, assert_is_true
from tools.assertions.department import assert_get_list_departments, assert_get_tree_departments
from tools.assertions.json import validate_json_schema


@pytest.mark.regression
@pytest.mark.department
@allure.tag(AllureTags.DEPARTMENT, AllureTags.REGRESSION)
class TestDepartment:
    """Класс тестов работы с отделами"""
    @allure.title("Get list departmens")
    def test_get_list_departments(self, department_client: DepartmentClient):
        #запрос
        response = department_client.get_list_departments()
        assert_status_code(response.status_code, HTTPStatus.OK)
        #Проверим по схеме
        response_data = GetListDepartmentsResponseSchema.model_validate_json(response.text)
        #что не пустой список (головное есть всегда)
        assert_is_true(response_data,"Список подразделений")

        assert_get_list_departments(response_data)
        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_data.model_json_schema())

    @allure.title("Get tree departments")
    def test_get_tree_departments(self, department_client: DepartmentClient):
        # запрос
        response = department_client.get_tree_departments()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetDepartmentTreeResponseSchema.model_validate_json(response.text)
        #тут сложная проверка всего дерева, сколько бы не было уровней children
        assert_get_tree_departments(response_data)

        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(),response_data.model_json_schema())

    @allure.title("Create new department")
    def test_create_new_department(self, department_client: DepartmentClient, list_departments: Department):
        #запрос
        request = CreateDepartmentRequestSchema(parent_department_id=list_departments.get_department_id)
        response = department_client.create_new_department(request)




