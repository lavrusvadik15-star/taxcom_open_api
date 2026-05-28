import allure

from clients.banners.banners_schema import GetBannersResponseSchema
from tools.assertions.base import assert_is_int, assert_is_true


@allure.step("Check body response")
def assert_get_banners(response: GetBannersResponseSchema):
    """Проверим данные массива баннеров"""

    banners = response.banners
    assert isinstance(banners,list), "Поле 'advisers' должно быть списком"

    # Выполнится если будет пусто в массиве адвайзеров
    if not banners:
        print("Массив подписантов пуст")
        return  # Выходим, если массив пуст

    # Проверяем каждый элемент массива
    for i, banner in enumerate(banners):
        assert_is_int(banner.priority, f"Приоритет для баннера {i}")
        assert_is_true(banner.content, f"Контент баннера {i}")