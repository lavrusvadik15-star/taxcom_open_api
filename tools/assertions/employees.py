from typing import Any

import allure

from clients.employees.employees_client import EmployeesClient
from clients.employees.employees_schema import GetListEmployeesResponseSchema, CreateEmployeeRequestSchema
from tools.assertions.base import assert_is_true, assert_is_guid


@allure.step("Check body response")
def assert_get_list_employees(response: GetListEmployeesResponseSchema):
    """"Проверим что там сотрудник, если есть"""
    employees = response.employees
    assert isinstance(employees, list),"Поле employees не является списком"

    # Выполнится если будет пусто в массиве адвайзеров
    if not employees:
        print("Массив сотрудников пуст")
        return  # Выходим, если массив пуст

    # Проверяем каждый элемент массива
    for i, employee in enumerate(employees):
        assert_is_true(employee.id, f"Айди сотрудника {i}")
        assert_is_true(employee.login, f"Логин пользователя {i}")

@allure.step("Check body response")
def assert_create_new_employee(response: CreateEmployeeRequestSchema):
    assert_is_guid(response,"В ответе нет айдишки нового юзера")
