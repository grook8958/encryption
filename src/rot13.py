import shift

# Chiffre en ROT13
def encrypt(text):
    return shift.encrypt(text, 13)

# Déchiffre en ROT13
def decrypt(code):
    return encrypt(code)