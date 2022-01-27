from os import system, popen, path

from const import CONFIG, TEST_PATH


class ConnectToScript:
    """Класс-коннектор. Для работы с тестируемым ПО."""

    def __init__(self):
        self.script_name = CONFIG['TESTING']['DATA']['name']
        self.path = TEST_PATH + self.script_name

    def chmod_command(self):
        result = path.exists(self.path)
        if result:
            system(f'chmod +x {self.path}')
        else:
            print(f'\nТестируемый файл {self.script_name} не найден.')
            assert result, 'Тестируемый файл не найден!'  # assert вместо sys.exit для добавления ошибки в allure

    def exec_script(self, *param):
        return popen(cmd=f"""{self.path} {' '.join(map(str, *param))}""").readlines()
