from http import HTTPStatus

import pytest
import allure

from clients.department.department_client import DepartmentClient
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code


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


