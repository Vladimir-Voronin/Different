import sys,os
razdel = ['_',':',';']
def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
def parol(words):
    new_words1 = []
    for i in words:
        new_words1.append(i)
        new_words1.append(i[0].upper() + i[1:])
        new_words1.append(i[0].upper() + i[1:-1] + i[-1].upper())
        new_words1.append(i.upper())
        new_words1.append

    new_words2 = []
    for j in new_words1:
        new_words2.append('123' + j + '123')
        new_words2.append(j + '123')
        new_words2.append(j + '1234')
        new_words2.append(j + '12345')
    new_words2 = new_words2 + new_words1
    return new_words2


opport = ['football','basketball']
opport_list = parol(opport)
print(opport_list)
##требование к паролю: min 6 символов, одна заглавня буква(min), одна цифра(min)
