import allure
import pytest
import pytest_check

from test_data.parametrize import type_param, sum_score_param, mapping_param, lenght_param, quantity_dice_param


@allure.title('Проверка количества костей участвующих в броске.')
@allure.description("""Позитивный тест проверяющий количество костей участвующих в бросках.
 Проверка по граничным значениям""")
@pytest.mark.parametrize('start, end', lenght_param)
def test_quantity_dice(send_param_fixture, start, end):
    assert end == len(send_param_fixture(1, start, end)[0].split(' = ')[0].split(' '))


@allure.title('Проверка маппинге значения выброшенного поля с количеством очков.')
@allure.description("""Позитивный тест проверяющий значения при маппинге различных результатов броска.""")
@pytest.mark.parametrize('var, res', mapping_param)
def test_quantity_score_throw_dice(send_param_fixture, var, res):
    for i in send_param_fixture(1, 1, 1):
        i = i.replace('\n', '').split(" = ")
        if i[0].count(var) == 1:
            assert i[1] == res, f"""Колчество очков за выпавшее значение {var} не правильное!\n
Ожидаемый результат: {res}\nФактический результат: {i[1]}"""
            break


@allure.title('Проверка мапинга значения выброшенных полей с количеством очков.')
@allure.description("""Позитивный тест проверяющий значения при получении различных результатов броска.""")
@pytest.mark.parametrize('param', sum_score_param)
def test_sum_score_throw_dice(send_param_fixture, param):
    for i in send_param_fixture(100000, *param):
        i = i.replace('\n', '').split(' = ')
        res_list = sorted(i[0].split(' '))
        if res_list != ['1', '2', '3', '4', '5']:
            control_sum = res_list.count('1') * 10 + res_list.count('5') * 5 + res_list.count('2') * 0 +\
                res_list.count('3') * 0 + res_list.count('4') * 0
            pytest_check.equal(control_sum, int(i[1]), f"""Ошибка!\nОжидаемый результат при количестве единиц
 равном {res_list.count('1')}, a пятёрок {res_list.count('5')}: {control_sum}\nФактический результат: {i[1]}\n
Результат броска: {res_list}""")


@allure.title('Проверка мапинга особой комбинации 1, 2, 3, 4, 5.')
@allure.description('Проверка мапинга особой комбинации 1, 2, 3, 4, 5.')
def test_special_combination_dice(send_param_fixture):
    flag = 0
    for i in send_param_fixture(100000, 5, 5):
        i = i.replace('\n', '').split(' = ')
        res_list = sorted(i[0].split(' '))
        if res_list == ['1', '2', '3', '4', '5']:
            assert 150 == int(i[1]), f"""Ошибка!\nОжидаемый результат: 150\nФактический результат: {i[1]}"""
            flag += 1
            break
    if flag == 0:
        assert False, 'Комбинация костей 1, 2, 3, 4, 5 не выпала!'


@allure.title('Проверка мапинга с различными типами данных.')
@allure.description('Проверка мапинга с различными типами данных.')
@pytest.mark.parametrize('param, error', type_param)
def test_type_param_dice(send_param_fixture, param, error):
    result = send_param_fixture(*param)
    assert result != error, f"""Ошибка при комбинации {param}!\nОжидаемый результат:
 результат броска одной кости и количество очков.\nФактический результат: {result}"""


@allure.title('Проверка колиества бросков костей.')
@allure.description('Проверка колиества бросков костей.')
def test_quantity_throw(send_param_fixture):
    lenght = len(send_param_fixture(1000, 5, 5))
    assert lenght == 1000, f"""Ошибка!\nОжидаемое количество бросков: 1000\n Фактическое количество бросков: {lenght}"""


@allure.title('Проверка наличия разного количества костей при различных диапазанах.')
@allure.description('Проверка наличия разного количества костей при различных диапазанах.')
@pytest.mark.parametrize('start, end', quantity_dice_param)
def test_all_quantity_dice(start, end, send_param_fixture):
    result = send_param_fixture(10000, start, end)
    test_list = []
    for i in result:
        i = i.replace('\n', '').split(' = ')
        if len(i) == 2:
            i = i[0].split(' ')
            test_list.append(len(i))
    assert len(set(test_list)) == end, f"""Ошибка!\n
Отсутствуют броски с количеством костей {set(test_list) - set(list(range(1, end)))}"""
