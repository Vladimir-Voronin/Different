import functools
import sys



trace_enabled = False
def trace(handle):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            print(func.__name__,args,kwargs,file = handle)
            return func(*args,**kwargs)
        return inner if trace_enabled == True else func
    return decorator


def trace2(func=None, *, handle=sys.stdout):
    #со скобками
    if func is None:
        return lambda func: trace2(func, handle=handle)

    #без скобок
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__,args,kwargs,file = handle)
        return func(*args,**kwargs)
    return inner


@trace2(handle = sys.stderr)
def someth(*args,**kwargs):
    print('i am func')
    print('i am printing ',args)
    print('and dict: ', kwargs)

kor = (1,4,6,3)
dictin = {'a': 1,'b': 2}
someth(*kor,**dictin)
