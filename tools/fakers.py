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

# Создаем экземпляр класса Fake с использованием Faker
# Локализация Faker('ru_RU')
fake = Fake(faker=Faker())