import random
def generat(n):
    checklist = []
    for i in range(n):
        checklist.append(i)
    print(checklist)
    resultlist = []
    while checklist:
        a = random.randint(0,n)
        if a in checklist:
            print(a)
            resultlist.append(a)
            checklist.remove(a)
        else:
            pass
    resultlist.sort()
    print(resultlist)

generat(100000)
