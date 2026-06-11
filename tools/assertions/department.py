import allure

from clients.department.department_schema import GetListDepartmentsResponseSchema, GetDepartmentTreeResponseSchema, \
    DepartmentNodeWithChildren, CreateDepartmentResponseSchema
from tools.assertions.base import assert_is_true, assert_is_guid


@allure.step("Check body response")
def assert_get_list_departments(response: GetListDepartmentsResponseSchema):
    """Проверим что там перечень департаментов"""
    departments = response.infos

    assert isinstance(departments, list), "Поле 'advisers' должно быть списком"
    # Тут не может не быть головного подразделения, так что проверять на пустоту нет смысла

    for i, department in enumerate(departments):
        assert_is_true(department.id,"id должен присутствовать")
        assert_is_true(department.name,"Имя подраздления обязательно")

# Это доп функция к assert_get_tree_departments. Она проверяет так же основной departement, и смотрит есть ли дети у подразделения
def check_node(node: DepartmentNodeWithChildren):
    """Рекурсивная функция проверки одного узла и всех его детей"""
    dept = node.department  # Берем данные отдела из обертки

    # Твои текущие проверки
    assert_is_true(dept.id, "id обязателен")
    assert_is_true(dept.name, "Название обязательно есть")

    # Если есть дети — запускаем проверку для них (рекурсия)
    if node.children:
        for child in node.children:
            check_node(child)  # функция вызывает сама себя

@allure.step("Check body response")
def assert_get_tree_departments(response: GetDepartmentTreeResponseSchema):
    """Проверем дерево отделов"""
    departments = response.department
    childrens = response.children

    assert_is_true(departments.id, "id обязателен")
    assert_is_true(departments.name, "Название обазательно есть")

    # Запуск рекурсивной проверки для всех детей
    if response.children:
        for child in response.children:
            check_node(child)

@allure.step("Check body response")
def assert_get_new_departemnt(response:CreateDepartmentResponseSchema):
    assert_is_guid(response.department_id, "ID департамента не guid")


