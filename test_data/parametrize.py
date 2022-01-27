"""В этом файле хранятся данные параметризации.
 Они вынесены в отдельный файл на случай переиспользования в других тестах."""

limit_value = [((10, 0, 1), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 0, 0), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 1, 0), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 1, -1), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, -1, 1), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((-10, 1, 1), ['Incorrect number of throws\n'], 'Граничные значения'),
               ((10, 0, 6), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 6, 0), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 6, 6), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 2, 1), ['Incorrect number of dices\n'], 'Граничные значения'),
               ((10, 'два', 4), ['Incorrect number of dices\n'], 'Некорректный тип данных'),
               ((10, 1, 'четыре'), ['Incorrect number of dices\n'], 'Некорректный тип данных'),
               ((10, 1), ['Incorrect number of arguments\n'], 'Некорректное количество переменных'),
               ((10, 1, 2, 3), ['Incorrect number of arguments\n'], 'Некорректное количество переменных'),
               ((), ['Incorrect number of arguments\n'], 'Некорректное количество переменных'), ]

type_param = [((1, '1one', '1один'), ['Incorrect number of dices\n']),
              ((1, 1, '1один'), ['Incorrect number of dices\n']),
              ((1, '1one', 1), ['Incorrect number of dices\n']),
              ((1, 1.7, 1), ['Incorrect number of dices\n']),
              ((1, 1, 1.7), ['Incorrect number of dices\n']),
              ((1, 1, 1.7), ['Incorrect number of dices\n']),
              (('42два', 1, 1), ['Incorrect number of throws\n']),
              ((4.5, 1, 1), ['Incorrect number of throws\n']),
              (('два', 1, 1), ['Incorrect number of throws\n']), ]

sum_score_param = [(1, 2), (1, 3), (1, 4), (1, 5)]

mapping_param = [('1', '10'), ('2', '0'), ('3', '0'), ('4', '0'), ('5', '5'), ('6', '0')]

lenght_param = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

quantity_dice_param = [(1, 2), (1, 3), (1, 4), (1, 5)]
