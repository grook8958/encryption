# Definie la table d'encryption par ligne
__table = [
    'ABCDEFGH',
    'IJKLMNOP',
    'QRSTUVWX',
    'YZ012345',
    '6789 !"#',
    '$%&\'()*+',
    ',-./:;<=',
    '>?@[\]^_'
]

# Fonction transformant chaine de charactères en une liste de liste représentant ligne et colonne
def __parseTable(table=[]):
    newTable = []
    for element in table:
        newTable.append([*element])
    return newTable

TABLE = __parseTable(__table)

# Retouve le code du charactère
def letter_code(char):
    for line in TABLE:
        for collumn in line:
            if (collumn == char):
                return (str(TABLE.index(line)+1), str(TABLE[TABLE.index(line)].index(collumn)+1))
    return char

# Chiffre avec le Carré de Polybe
def encrypt(text=''):
    if len(text) <= 0:
        return None
    chars = [*text.upper()]
    code = []
    for char in chars:   
        code.append(''.join(letter_code(char)))
    return ' '.join(code)

# Déchiffre avec le Carré de Polybe
def decrypt(code=''):
    if len(code) <= 0:
        return None
    if (' ' in code): 
        C = code.split(' ')
    else:
        C = __resolveCode(code)
    chars = []
    for code in C:
        chars.append(TABLE[int(code[0])-1][int(code[1])-1].lower())
    return ''.join(chars)

# Renvoie le code chiffré par doublets de chiffres
def __resolveCode(code):
    a = [*code]
    arr = []
    for i in range(int(len(a))):
        if (i % 2 == 0):
            arr.append(a[i]+a[i+1])
    return arr