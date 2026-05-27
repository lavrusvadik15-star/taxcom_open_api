import allure

from clients.advisers.advisers_schema import GetAdviserSubscriptionResponseSchema
from tools.assertions.base import assert_is_true, assert_equal, assert_is_int


@allure.step("Check body response")
def assert_advisers_subscription(response: GetAdviserSubscriptionResponseSchema):
    """проверим что данные присутсвтвуют"""
    assert_is_true(response.adviser, "Массив подписанных адвайзеров")
    assert_is_int(response.adviser[0].adviser_id, "ID Адвайзера")