# Tableau de Chiffrement 
__table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Transforme le tableau en liste de charactère
TABLE = [*__table]

# Trouve l'index de la lettre dans le tableau
def __resolveIndex(letter):
    return TABLE.index(letter.upper())

# Enleve tout charactère de la clé d'encryption non-pris en charge
def __validateKey(key):
    k = []
    for char in key:
        if char.upper() in TABLE:
            k.append(char)
    return k

# Chiffre en Vigenere avec une clé de chiffrement donné
def encrypt(text, key):
    key = __validateKey(key)
    code = [*text]
    j = 0
    for i in range(len(code)):
        if code[i].upper() in TABLE:
            x = (__resolveIndex(code[i])+__resolveIndex(key[j%len(key)]))%26
            if code[i].isupper(): code[i] = TABLE[x]
            else: code[i] = TABLE[x].lower()
            j += 1
    return ''.join(code)

# Déchiffre en Vigenere avec une clé de chiffrement donné
def decrypt(code, key):
    key = __validateKey(key)
    text = [*code]
    j = 0
    for i in range(len(text)):
        if text[i].upper() in TABLE:
            x = (__resolveIndex(text[i])-__resolveIndex(key[j%len(key)]))%26
            if text[i].isupper(): text[i] = TABLE[x]
            else: text[i] = TABLE[x].lower()
            j += 1
    return ''.join(text)