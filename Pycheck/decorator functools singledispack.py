import functools

'''@functools.singledispack нужен для создания
обобщенных функций, то есть фунций, которые
ведут себя по разному, если им передают аргументы
разного типа.
Пример такой функции в стандартной библиотеки Python:
функция sum может складывать числа int, числа float,
складывать списки, может что-то еще'''

@functools.singledispatch
def lol(obj):
    '''Эта функция будет возвращать аргумент
    и подпись lol, если тип аргумента int.
    Если это список она будет возвращать
    каждое из значений списка с подписью lol'''
    type_name= type(obj).__name__
    assert False, "Unsupported type " + type_name


@lol.register(int)
def _(obj):
   return str(obj) + ' lol'


@lol.register(list)
def _(obj):
    result = ''
    for i in obj:
        result = result + str(i) + ' lol '
    return result
















