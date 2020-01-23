def XOR_cipher():
    stroka = input('Введите текст который необходимо зашифровать: ')
    klu4 = int(input('Введите ключ шифрования : '))
    crypt = ''
    for i in stroka:
        try:
            crypt += chr(ord(i)^ord(klu4))
        except TypeError:
            crypt += chr(ord(i)^klu4)
    print(crypt)

    decrypt = ''
    for x in crypt:
        try:
            decrypt += chr(ord(x)^ord(klu4))
        except TypeError:
            decrypt += chr(ord(x) ^ klu4)
    print(decrypt)
#XOR_cipher()
XOR_cipher()
