import allure

from assertions.base import assert_is_true, assert_is_guid
from clients.contacts.contact_schema import GetContactListResponseSchema, GetContactListAsDictionaryItemsResponseSchema


@allure.step("Check body response")
def assert_get_list_contacts(response: GetContactListResponseSchema):
    """Проверим что в ответе у нас точно контакта данные"""
    contacts = response.contacts

    assert isinstance(contacts,list), "Поле должно быть списком"

    for i, contact in enumerate(contacts):
        assert_is_true(contact.edx_client_id, "EDX нет")


@allure.step("Check body response")
def assert_get_low_list_contacts(response: GetContactListAsDictionaryItemsResponseSchema):
    """Проверим ответ простого представления списка контактов"""
    contacts = response.contact_low
    assert isinstance(contacts,list)
    for i, contact in enumerate(contacts):
        assert_is_true(contact.id, "ID нет")
        assert_is_guid(contact.id, "ID не корректного формата")