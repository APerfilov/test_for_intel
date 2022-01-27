import os
from utils.reader import read_yaml


def get_project_path():
    """Получение абсолютного пути."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)))


"""Константы необходимые для получения пути к файлу config.yaml и к папке с тестируемыми скриптами."""
CONFIG = read_yaml(path=os.path.join(os.path.dirname(os.path.abspath(__file__))) + '/config.yaml')
TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__))) + '/test_script/'
