import functools
import time

timethis_enabled = True
def timethis(func=None, *, n_iner = 100):
    if func is None:
        return lambda func: timethis(func, n_iner=n_iner)

    @functools.wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__, end=' ... ')
        acc = float('inf')
        for i in range(n_iner):
            tick = time.perf_counter()
            result = func(*args,**kwargs)
            acc = min(acc,time.perf_counter() - tick)
        print(acc)
        return result
    return inner if timethis_enabled == True else func

@timethis(n_iner = 12)
def lom(*args):
    res = 0
    for i in args:
        res += i
    return res

a = lom(1,8,6)
print(a)

        
