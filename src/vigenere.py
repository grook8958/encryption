__table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

TABLE = [*__table]

def __resolveIndex(letter):
    return TABLE.index(letter.upper())

def encrypt(text, key):
    key = [*key]
    code = [*text]
    j = 0
    for i in range(len(code)):
        if code[i].upper() in TABLE:
            x = (__resolveIndex(code[i])+__resolveIndex(key[j%len(key)]))%26
            code[i] = TABLE[x]
            j += 1
    return ''.join(code)


def decrypt(code, key):
    key = [*key]
    text = [*code]
    j = 0
    for i in range(len(text)):
        if text[i].upper() in TABLE:
            x = (__resolveIndex(text[i])-__resolveIndex(key[j%len(key)]))%26
            text[i] = TABLE[x]
            j += 1
    return ''.join(text)