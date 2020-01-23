def make_min(*,lo,hi):
    def inner(first,*args):
        res = hi
        for arg in (first,) + args:
            if arg < res and lo < arg < hi:
                res = arg
            return max(res,lo)
    return inner

def coloriz(retcolor):
    color = retcolor
    print('Your color is ',color)
    def changecolor(cmyk = 0):
        nonlocal color
        color = color + cmyk
        print('Your change color to ',color)
        return color
    changecolor()
    return changecolor

### сверху coloriz которая обходит глобальную переменную, снизу тоже самое но с глобальной переменной

### Я НИЧЕГО НЕ ПОНИМАЮ
