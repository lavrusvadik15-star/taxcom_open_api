import allure

from clients.auth.auth_schema import LoginResponseSchema
from tools.assertions.base import assert_is_true, assert_equal


@allure.step("Chek body response login")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверка ответа на запрос авторизации (что токен не пустой)
    :param response:
    :return:
    """
    assert_is_true(response.token, "Token")

@allure.step("Chek body response Access Denied")
def assert_login_response_access_denied(response: LoginResponseSchema):
    """
    Проверка тело запроса при невалидном abonent_id
    :param response:
    :return:
    """
    assert_equal(actual=response.result, expected="AccessDenied")