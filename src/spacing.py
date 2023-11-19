__table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

TABLE = [*__table]

def __resolveIndex(letter):
    return TABLE.index(letter.upper())

def encrypt(text, sub):
    code = [*text]
    for i in range(len(code)):
        if code[i].upper() in TABLE:
            x = (__resolveIndex(code[i])+sub)%26
            code[i] = TABLE[x]
    return ''.join(code)


def decrypt(code, sub):
    text = [*code]
    for i in range(len(text)):
        if text[i].upper() in TABLE:
            x = (__resolveIndex(text[i])-sub)%26
            text[i] = TABLE[x]
    return ''.join(text)