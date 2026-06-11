from faker import Faker


# Мы создаем класс Fake, который инкапсулирует логику работы с библиотекой Faker.
# Этот класс будет использоваться для генерации случайных данных, таких как имена, email, пароли, и другое
class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        Экземпляр класса Faker
        """
        self.faker = faker
    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.
        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def integer(self, start: int = 1, end: int= 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.
        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)

    def password(self) -> str:
        """
        Генерирует случайный пароль.
        :return: Случайный пароль.
        """
        return self.faker.password()

    def word(self) -> str:
        """
        Герениурется рандомное слово
        :return: рандомное слово строкой
        """
        return self.faker.word()

    def uuid(self) -> str:
        """
        Геирируется UUID4 ранмный
        :return:
        """
        return self.faker.uuid4()

    def kpp(self) ->str:
        """Генериует KPP
        :return: KPP"""
        tax_authority_code = self.faker.random_int(min=1000, max=9999)  # Код налогового органа
        reason_code = self.faker.random_int(min=1, max=50)  # Причина постановки на учет (1-50)
        record_number = self.faker.random_int(min=1, max=999)  # Порядковый номер

        return f"{tax_authority_code:04d}{reason_code:02d}{record_number:03d}"

    def address(self) -> str:
        """Генерируется адрес
        :return: Адрес"""
        return self.faker.address()

# Создаем экземпляр класса Fake с использованием Faker
# Локализация Faker('ru_RU')
fake = Fake(faker=Faker())