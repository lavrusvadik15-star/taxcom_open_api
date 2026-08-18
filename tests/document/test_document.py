import datetime
from datetime import datetime

import allure
import pytest
from httpx import request

from clients.document.document_client import DocumentClient
from clients.document.document_schema import CreateDocumentRequestSchema, DocumentType
from tools.allure_utils.tags import AllureTags


@pytest.mark.regression
@pytest.mark.document
@allure.tag(AllureTags.DOCUMENT, AllureTags.REGRESSION)
class TestDocument:
    """Класс тестов с документами"""

    @allure.title("Create Nonformalized")
    def test_create_nonformalized_document(self, document_cert_client: DocumentClient):
        request = CreateDocumentRequestSchema(
            document_type= DocumentType.CONTRACT,
            document_number="123",
            document_sum="1000",
            document_date=datetime.now(),
            receiver_abonent_id="6D720756-E958-43C3-B72D-5C3AD4F40E0F",
            resign_required=True,
            attachment_file_name="",  # временно пусто
            attachment_file_content=""  # временно пусто
        )

        # Отправляем с файлом из testdata
        file_path = "testdata/jpg1.jpg"
        response = document_cert_client.create_nonformalized_document(request, file_path)
        print(response.content)