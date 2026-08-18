import allure

from clients.abonent.abonent_schema import GetAbonentRequisitesResponseSchema, AvailableDepartmentsResponseSchema, \
    GetMobileQRResponseSchema, GetAutopilotStatusResponseSchema
from clients.advisers.advisers_schema import GetAdviserSubscriptionResponseSchema
from tools.assertions.base import assert_is_true, assert_is_boolean, assert_equal


@allure.step("Check body response get abonent requisites")
def assert_abonent_requisites(response: GetAbonentRequisitesResponseSchema):
    """Проверим что в ответе есть данные"""
    assert_is_true(response.inn, "ИНН")

@allure.step("Check body response")
def assert_available_departments(response: AvailableDepartmentsResponseSchema):
    """Проверим что данные присутствуют, если есть"""
    #Что поле вообще есть (пустое или нет)
    assert response.items is not None, "Список отделений отсутствует"
    # На пустоту
    if not response.items:
        allure.attach("Список отделений пуст",
                      name="Info",
                      attachment_type=allure.attachment_type.TEXT)
        return
    # Если подразделения есть
    for idx, department in enumerate(response.items):
        assert department.id, f"У отделения {idx + 1} отсутствует ID"

@allure.step("Check body response")
def assert_get_mobile_qr(response: GetMobileQRResponseSchema):
    """проверим что данные присутсвтвуют"""
    assert_is_true(response.qr, "QR код")

@allure.step("Check body response")
def assert_get_autopilot_status(response: GetAutopilotStatusResponseSchema):
    """Проверка статуса автопилота"""
    assert_is_boolean(response.is_on, "Статус подключения ассистента и сдк")


