import time

def lis():
    mylist = [x*x for x in range(100)]
    for i in mylist:
        return i


def generat():
    mygenerat = (x*x for x in range(100))
    for i in mygenerat:
        return i
def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

if __name__ == '__main__':
    a = lis()
    b = generat()
    c = createGenerator()
    print(c)
    for i in c:
        print(i)
    
