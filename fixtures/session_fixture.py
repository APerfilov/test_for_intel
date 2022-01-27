import allure
import pytest

from connect.connect import ConnectToScript


@allure.title('Фикстура делающая тестируемый файл исполняемым. Срабатывает один ращ перед прогоном тестов.')
@pytest.fixture(scope='session')
def chmod_x_fixture():
    return ConnectToScript().chmod_command()
