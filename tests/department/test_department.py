from http import HTTPStatus
import json
import pytest
import allure

from clients.department import department_client
from clients.department.department_client import DepartmentClient
from clients.department.department_schema import GetListDepartmentsResponseSchema, GetDepartmentTreeResponseSchema, \
    CreateDepartmentRequestSchema, CreateDepartmentResponseSchema, UpdateDepartmentRequestSchema, \
    DeleteDepartmentRequestSchema
from fixtures.department import Department, NewDepartment
from tools.allure_utils.tags import AllureTags
from tools.assertions.base import assert_status_code, assert_is_true, assert_is_guid
from tools.assertions.department import assert_get_list_departments, assert_get_tree_departments, \
    assert_get_new_departemnt
from tools.assertions.json import validate_json_schema
from tools.fakers import fake


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
        print(response_data)
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
        assert_status_code(response.status_code, HTTPStatus.OK)

        #Т.к. в ответе просто приходится id нового департамента, то обернем его
        raw_data = json.loads(response.content)
        wrapped_data = {"department_id": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку
        response_data = CreateDepartmentResponseSchema.model_validate_json(json_wrapped)

        #Проверим, что вернулся guid департамента
        assert_get_new_departemnt(response_data)
        print(response_data)
        # Дополнительно проверяем, что тело ответа сервера соответствует ожидаемой JSON-схеме
        validate_json_schema(wrapped_data,response_data.model_json_schema())

    @allure.title("Update department")
    def test_update_department(self, list_departments: Department, department_client: DepartmentClient, create_department: NewDepartment):
        request = UpdateDepartmentRequestSchema(#department_id=create_department.get_new_department_id,
                                                department_id= list_departments.get_new_department_id,
                                                parent_department_id=list_departments.get_department_id,
                                                name = fake.word())
        response = department_client.update_department(request)
        print(response)
        #Тут апдейт ничего не отвечает, без проверок (или добавить опять вызов листа, что там новое имя)
        assert_status_code(response.status_code, HTTPStatus.OK)

    #Тест на удаление готов, но сделать его можно только при авторизации под сертификатом, добавить
    @allure.step("Delete department")
    def test_delete_department(self,list_departments: Department,
                               department_cert_client: DepartmentClient,
                               create_department: NewDepartment):

        name = create_department.get_name_new_department
        id = None

        #смотрим все подразделения с нашим созданным из теста ранее
        list = department_cert_client.get_list_departments()
        list_data = GetListDepartmentsResponseSchema.model_validate_json(list.text)
        #ищем айди нового подразделения что мы создали
        for i in list_data.infos:
            if i.name == name:
                id = i.id
                break

        request = DeleteDepartmentRequestSchema(department_id=id,
                                                move_employees_to_department_id= list_departments.get_department_id)
        response = department_cert_client.delete_department(request)
        #тут пустая строка, но пусть будет на будущее
        response_raw = response.content.decode('utf-8')
        #ответ пустой, можно без проверокю (или добавить опять вызов листа, что там нет подразделения с таким id)
        assert_status_code(response.status_code, HTTPStatus.OK)








