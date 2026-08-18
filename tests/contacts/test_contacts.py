import json
from http import HTTPStatus

import allure
import pytest

from tools.allure_utils.tags import AllureTags
from assertions.base import assert_status_code
from assertions.contacts import assert_get_list_contacts, assert_get_low_list_contacts
from clients.contacts.contact_client import ContactClient
from clients.contacts.contact_schema import GetContactListRequestSchema, GetContactListResponseSchema, \
    GetContactListAsDictionaryItemsResponseSchema


@pytest.mark.regression
@pytest.mark.contacts
@allure.tag(AllureTags.CONTACTS, AllureTags.REGRESSION)
class TestContacts:
    """Класс тестов с контактами"""

    @allure.title("Get list contacts")
    def test_get_contact_list(self, contacts_cert_client: ContactClient) :
        #запрос
        request = GetContactListRequestSchema(statusFilters= ["All"], searchText= "2AL-6D720756-E958-43C3-B72D-5C3AD4F40E0F-00000")
        response = contacts_cert_client.get_contact_list(request)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetContactListResponseSchema.model_validate_json(response.text)
        assert_get_list_contacts(response_data)

    @allure.title("Get Contact Invitations")
    def test_get_contact_invitations(self, contacts_cert_client: ContactClient) :
        response = contacts_cert_client.get_contact_invitations()
        assert_status_code(response.status_code, HTTPStatus.OK)
        #зачем эта штука вообще нужна для главной страницы?

    @allure.title("Get Contact List As Dictionary Items")
    def test_get_contact_list_as_dictionary(self, contacts_cert_client: ContactClient) :
        response = contacts_cert_client.get_contact_list_as_dictionary()
        assert_status_code(response.status_code, HTTPStatus.OK)

        #обернуть в объект
        raw_data = json.loads(response.content)
        wrapped_data = {"contact_low": raw_data}  # оборачиваем массив в объект
        json_wrapped = json.dumps(wrapped_data)  # снова преобразуем в JSON‑строку

        response_data = GetContactListAsDictionaryItemsResponseSchema.model_validate_json(json_wrapped)
        assert_get_low_list_contacts(response_data)

