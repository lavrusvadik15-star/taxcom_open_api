# Этот файл относится к пакету Фикстур
# В нем добавлены плагины, чтобы можно было подключать фикстуры из отдельных файлов
# Тут мы указываем, что фикстуры находятся в таком то модуле

# И вот фикстуры станут доступны глобально для любого теста, независимо где что находится
# Так избегают иерархичности, чтобы не запутиться в фикстурах
pytest_plugins = (
    "fixtures.auth",
    "fixtures.abonent",
    "fixtures.advisers",
    "fixtures.banners",
    "fixtures.department",
    "fixtures.employees",
    "fixtures.crypto",
    "fixtures.contacts",
    "fixtures.document"
)



import sys
from pathlib import Path

# Добавляем корневую папку проекта в PYTHONPATH
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

# Также добавляем папку tools, если нужно
tools_dir = root_dir / 'tools'
sys.path.insert(0, str(tools_dir))