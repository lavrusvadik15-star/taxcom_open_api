import allure
import pytest
from httpx import request

from clients.document.document_client import DocumentClient
from clients.document.document_schema import CreateDocumentRequestSchema
from tools.allure_utils.tags import AllureTags


@pytest.mark.regression
@pytest.mark.document
@allure.tag(AllureTags.DOCUMENT, AllureTags.REGRESSION)
class TestDocument:
    """Класс тестов с документами"""

    @allure.title("Create Nonformalized")
    def test_create_nonformalized_document(self, document_cert_client: DocumentClient):
        request = CreateDocumentRequestSchema()
        response = document_cert_client.create_nonformalized_document(request)
        print(response.content)