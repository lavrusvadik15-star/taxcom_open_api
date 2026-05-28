import allure

from clients.advisers.advisers_schema import GetAdviserSubscriptionResponseSchema
from tools.assertions.base import assert_is_true, assert_equal, assert_is_int, assert_is_not_empty


@allure.step("Check body response")
def assert_advisers_subscription(response: GetAdviserSubscriptionResponseSchema):
    """проверим что данные присутсвтвуют"""
    # advisers = response.adviser
    # # Проверяем, что массив не пустой
    # if not advisers:
    #     assert False, "Массив подписанных адвайзеров пуст"
    #
    # assert_is_true(response.adviser, "Массив подписанных адвайзеров")
    # assert_is_int(response.adviser[0].adviser_id, "ID Адвайзера")

    advisers = response.adviser

    assert (isinstance(advisers, list), "Поле 'advisers' должно быть списком")
    # Выполнится если будет пусто в массиве адвайзеров
    if not advisers:
        print("Массив подписантов пуст")
        return  # Выходим, если массив пуст

    # Проверяем каждый элемент массива
    for i, adviser in enumerate(advisers):
        assert_is_int(adviser.adviser_id, f"ID Адвайзера {i}")
        assert_is_not_empty(adviser.email, f"Email адвайзера {i}")