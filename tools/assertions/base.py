from typing import Any, Sized

import allure


#Это файл с функциями различных проверок для инкапсуляции их. Чтобы вызывать функцию, а не прописывать каждый раз все отдельно

@allure.step("Check that response status code")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.
    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    """
    assert actual == expected, (
        f"Статут код {actual} отличается от ожидаемого -{expected}"
    )

@allure.step("Equality check {actual} and {expected}")
def assert_equal(actual: Any, expected: Any):
    """
    Проверяем равенство двух объектов
    :param actual:
    :param expected:
    :return:
    """
    assert actual == expected, (f"Значения разные, {actual}, а ожидалось- {expected}")

@allure.step("Check {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Проверить что значение не пустое
    (передаем имя переменной так же для ясности)
    :param actual:
    :return:
    """
    assert actual, (f"{name}-пусто!")

@allure.step("Check {name} is boolean")
def assert_is_boolean(actual: Any, name: str):
    """Проверить, что объект является булевым значением
    :param actual:
    :param name:
    :return:
    """
    assert isinstance(actual, bool), (f'{name} не булево значение')


@allure.step("Check length")
def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверим длину объекта (Sized кастомный специальный тип из библиотеки)
    Те типы, у которых может быть длина.
    :param actual:
    :param expected:
    :param name:
    :return:
    """
    #так как мы передаем динамическое значение (длину списка), то шаг добавим через менеджера
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):

        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )