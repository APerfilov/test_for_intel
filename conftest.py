def pytest_make_parametrize_id(val):
    """Не удалять! Функция позволяет адекватно читать русскоязычный текст при выводе"""
    return repr(val)


pytest_plugins = ['fixtures.session_fixture', 'fixtures.function_fixture', ]
