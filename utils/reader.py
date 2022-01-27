import yaml


def read_yaml(path):
    """Утилита для чтения yaml."""
    with open(path, 'r', encoding='UTF-8') as config:
        data = config.read()
        return yaml.load(data, Loader=yaml.FullLoader)
