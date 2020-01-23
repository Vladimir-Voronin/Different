import functools


mydecor_enabled = True
def mydecor(func):
    #Заменяем __name__, __doc__ и __module__
    #С помощью декоратора из модуля
    @functools.wraps(func)
    def define(*args):
        print('Your info: ', func.__name__, args)
        proverka = True
        for arg in args:
            if type(arg) is not int:
                proverka = False
                break

        if proverka:
            print('This is int function')
        return func(*args)
    return define if mydecor_enabled is True else func


@mydecor
def num(*args):
    '''Сумма всех чисел'''
    res = 0
    for arg in args:
       res += arg 
    return res


@mydecor
def ymn(*args):
    '''Произведение всех чисел'''
    res = 1
    for arg in args:
       res *= arg 
    return res

a = num(5,7,6)
print(a)
b = ymn(2,3,4)
print(b)
