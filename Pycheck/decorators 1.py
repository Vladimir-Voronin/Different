import functools

def mydecor(func):
    def define(*args):
        print('Your info: ', func.__name__, args)
        proverka = True
        for arg in args:
            if type(arg) is int:
                pass
            else:
                proverka = False
                break
        if proverka:
            print('This is int function')
        return func(*args)
    functools.update_wrapper(define, func)
    #Этот метод перезаписывает:
    #define.__module__ = func.__module__
    #define.__name__ = func.__name__
    #define.__doc__ = func.__doc__
    return define

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
