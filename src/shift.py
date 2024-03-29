# Tableau de Chiffrement 
__table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Transforme le tableau en liste de charactère 
TABLE = [*__table]

# Trouve l'index de la lettre dans le tableau
def __resolveIndex(letter):
    return TABLE.index(letter.upper())

# Chiffre en décallant chaque lettre de n rangs
def encrypt(text, shift):
    code = [*text]
    for i in range(len(code)):
        if code[i].upper() in TABLE:
            x = (__resolveIndex(code[i])-shift)%26
            if code[i].isupper(): code[i] = TABLE[x]
            else: code[i] = TABLE[x].lower()
    return ''.join(code)

# Déchiffre en décalant chaque lettre n rangs
def decrypt(code, shift):
    text = [*code]
    for i in range(len(text)):
        if text[i].upper() in TABLE:
            x = (__resolveIndex(text[i])+shift)%26
            if text[i].isupper(): text[i] = TABLE[x]
            else: text[i] = TABLE[x].lower()
    return ''.join(text)