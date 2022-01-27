import allure
import pytest

from test_data.parametrize import limit_value


@allure.title('Проверка ответа скрипта при вводе не валидных значений. {type_test}.')
@pytest.mark.parametrize('data_turple, error, type_test', limit_value)
def test_limit_value_neg(data_turple, error, type_test, send_param_fixture):
    response = send_param_fixture(*data_turple)
    assert error == response,\
        f"""Текст ошибки не корректен!\nОжидаемый результат: {error}\nФактический результат: {response}"""
