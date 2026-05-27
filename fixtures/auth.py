import pytest
from pydantic import BaseModel

from clients.auth.auth_client import get_auth_client, AuthClient, get_private_auth_client, PrivateAuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema


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

