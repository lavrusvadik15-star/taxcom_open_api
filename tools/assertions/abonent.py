import allure

from clients.abonent.abonent_schema import GetAbonentRequisitesResponseSchema, AvailableDepartmentsResponseSchema, \
    GetMobileQRResponseSchema, GetAutopilotStatusResponseSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_is_boolean


@allure.step("Check body response get abonent requisites")
def assert_abonent_requisites(response: GetAbonentRequisitesResponseSchema):
    """Проверим что в ответе есть данные"""
    assert_is_true(response.inn, "ИНН")

@allure.step("Check body response")
def assert_available_departments(response: AvailableDepartmentsResponseSchema):
    """Проверим что данные присутствуют"""
    assert_is_true(response.items, "Список отделений")

@allure.step("Check body response")
def assert_get_mobile_qr(response: GetMobileQRResponseSchema):
    """проверим что данные присутсвтвуют"""
    assert_is_true(response.qr, "QR код")

@allure.step("Check body response")
def assert_get_autopilot_status(response: GetAutopilotStatusResponseSchema):
    """Проверка статуса автопилота"""
    assert_is_boolean(response.is_on, "Статус подключения ассистента и сдк")

