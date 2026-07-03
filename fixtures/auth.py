import base64
import json

import pytest
from pydantic import BaseModel

from clients.auth.auth_client import get_auth_client, AuthClient, get_private_auth_client, PrivateAuthClient, \
    get_private_auth_cert_client
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, LoginCertificateRequestSchema, \
    LoginCertificateResponseSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema
from clients.private_http_builder_with_cert import private_client_with_cert
from tools.crypto_pro import decrypt_and_get_bytes


class CabinetSchema(BaseModel):
    request: LoginRequestSchema
    response: LoginResponseSchema

    @property
    def token(self) -> str:
        token = self.response.token
        return (f"Bearer {token}")

    @property
    def credentials(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            login=self.request.login,
            password=self.request.password
        )

@pytest.fixture(scope="function")
def public_auth_client() -> AuthClient:
    """Создает публичный АПИ клиент для авторизации"""
    # Создаем новый API клиент для работы с аутентификацией
    return get_auth_client()


@pytest.fixture
def auth_cabinet(public_auth_client: AuthClient) -> CabinetSchema:
    """Захардкоженный логин в кабинет пользователя"""
    login_request = LoginRequestSchema(
        login="ad9511df-5507-44be-96ae-ddc8410ae38c",
        password="kR1Zd1WoWdMdpTvWfkxx"
    )
    # Авторизация через API по кредам
    login_response = public_auth_client.login_api(login_request)
    # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
    json_string_response = login_response.content.decode('utf-8')
    # преобразование строки JSON в словарь, но тут не надо, кажется
    # data = json.loads(json_string_response)
    # Десериализация JSON-ответа в объект LoginResponseSchema
    login_response_data = LoginResponseSchema.model_validate_json(json_string_response)
    return CabinetSchema(request=login_request,response=login_response_data)

@pytest.fixture
def private_auth_client(auth_cabinet: CabinetSchema) -> PrivateAuthClient:
    """Создаем приватный api-клиента по кредам кабинета от фикстуры авторизации, вытащив из нее данные"""
    return get_private_auth_client(auth_cabinet.credentials)

class AuthCertificateSchema(BaseModel):
    """Вспомогательная модель данных ответов на запрос авторизации по сертификата"""
    request: LoginCertificateRequestSchema
    response: LoginCertificateResponseSchema
    raw_token: str # тут токен после расшифровки получим

    @property
    def token(self) -> str:
        return f"Bearer {self.raw_token}"
    # @property
    # def token(self) -> str:
    #     token  = self.response.token
    #     return (f"Bearer {token}")
    # @property
    # def raw_token(self) -> str:
    #     # Чистый токен без префикса
    #     return self.response.token

@pytest.fixture
def certificate_base64_str() -> str:
    from pathlib import Path
    cert_path = Path("testdata") / "Soloviev_test.cer"
    if not cert_path.exists():
        raise FileNotFoundError(f"Сертификат не найден: {cert_path.absolute()}")
    cert_bytes = cert_path.read_bytes()
    return base64.b64encode(cert_bytes).decode("ascii")

@pytest.fixture
def test_login_with_certificate(
    public_auth_client,
    certificate_base64_str: str
) -> AuthCertificateSchema:
    login_request = LoginCertificateRequestSchema(
        is_cert_new_qes=True,
        is_cloud=None,
        abonent_id="8260214A-2575-45DF-9E56-657D5B4810B8",
        email=None,
        certificate_public_key=certificate_base64_str,
    )

    login_response = public_auth_client.login_certificate_api(login_request)
    response_data = login_response.json()

    if response_data.get("result") != "Success":
        raise RuntimeError(f"Авторизация не удалась: {response_data}")

    response_schema = LoginCertificateResponseSchema.model_validate(response_data)

    # --- ЗДЕСЬ ГЛАВНОЕ: расшифровываем CMS ---
    thumbprint = "0a48db5859f13bca349b41a0de8cadfa45bb9c69"
    cert_store = "my"

    encrypted_cms_base64 = response_schema.token

    decrypted_bytes = decrypt_and_get_bytes(encrypted_cms_base64, thumbprint, cert_store)

    # --- ИСПРАВЛЕНИЕ ЗДЕСЬ ---
    # decrypted_bytes — это уже готовый JWT-токен в байтах.
    # Просто декодируем в строку. НЕ делаем json.loads!
    raw_token = decrypted_bytes.decode("utf-8").strip()

    return AuthCertificateSchema(
        request=login_request,
        response=response_schema,
        raw_token=raw_token,  # передаём сам JWT
    )


@pytest.fixture
def private_auth_cert_client(test_login_with_certificate: AuthCertificateSchema) -> PrivateAuthClient:
    """Собирает готовый приватный клиент на основе успешного логина"""
    raw_token = test_login_with_certificate.raw_token

    # Создаём базовый httpx клиент через чистую функцию
    http_client = private_client_with_cert(raw_token)

    # Оборачиваем в кастомный клиент
    return get_private_auth_cert_client(http_client)


