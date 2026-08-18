from enum import Enum

# Так принято хранить используемые теги в отчете
class AllureTags(str, Enum):
    REGRESSION = "REGRESSION"

    AUTH = "AUTH"
    LOGIN = "LOGIN"
    ABONENT = "ABONENT"
    ADVISERS = "ADVISERS"
    BANNERS = "BANNERS"
    DEPARTMENT = "DEPARTMENT"
    EMPLOYEES = "EMPLOYEES"
    CONTACTS = "CONTACTS"