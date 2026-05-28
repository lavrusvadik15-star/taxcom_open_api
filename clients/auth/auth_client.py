import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.auth.auth_schema import LoginRequestSchema, LoginCertificateRequestSchema, LoginResponseSchema
from clients.private_http_builder_no_cert import AuthenticationUserSchema, get_private_http_client_no_cert
from clients.public_http_builder import get_public_http_client


class AuthClient(ApiClient):
    """
    Работа с /api/Auth
    """
    @allure.step("Auth from login-password")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод авторизации из логина и пароля
        :param request: Словарь с емейлом и паролем
        :return: Ответ от сервера
        """
        return self.post(url="/api/Auth/login",
                         #Сериализуем класс LoginRequestSchema, нашу pydantic модель, в json
                         # т.к. там у нас поле с alias
                         json=request.model_dump(by_alias=True))

    @allure.step('Login with certificate')
    def login_certificate_api(self, request: LoginCertificateRequestSchema) -> Response:
        """
        Метод аторизаци по сертификатам
        :param request: Словарь с данными о сертификате
        :return: ответ от сервера
        """
        return self.post(url="/api/Auth/loginByCertificate",
                         json=request.model_dump(by_alias=True))


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema :
        """Метод, чтобы сразу извлекать нужные поля из логина, чтобы не парсить весь response"""
        login_response = self.login_api(request)
        # Декодируем пришедшую байтовую строку байтовой строку в обычную строку
        json_string_response = login_response.content.decode('utf-8')
        # преобразование строки JSON в словарь, но тут не надо, кажется
        # data = json.loads(json_string_response)
        # Десериализация JSON-ответа в объект LoginResponseSchema
        login_response_data = LoginResponseSchema.model_validate_json(json_string_response)
        return login_response_data

class PrivateAuthClient(ApiClient):
    """
    Работа с приватными /api/Auth
    """
    @allure.step('Get abonent permission')
    def get_abonent_permission(self) -> Response:
        """
        Мето получения прав абонента
        :return: ответ от сервера
        """
        return self.get(url="/api/Auth/getAbonentPermissions")






# Добавляем builder для AuthenticationClient с публичным клиентом
def get_auth_client() -> AuthClient:
    """
    создаёт экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return AuthClient(client=get_public_http_client())

# Клиент для работы с закрытым апи авторизации по кредам
def get_private_auth_client(user : AuthenticationUserSchema) -> PrivateAuthClient:
    """Создает уже авторизованный клиент для запросов апи auth после авторизации"""
    return PrivateAuthClient(client=get_private_http_client_no_cert(user))