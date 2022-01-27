import allure
import pytest

from connect.connect import ConnectToScript


@allure.title('Фикстура отправляющая тестовые значения.')
@pytest.fixture()
def send_param_fixture(chmod_x_fixture):
    def _send_param(*param):
        return ConnectToScript().exec_script(param)
    return _send_param
