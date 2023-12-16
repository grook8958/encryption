import shift

# Chiffre en ROT13
def encrypt(text):
    return shift.encrypt(text, 13)

# Déchiffre en ROT13
def decrypt(code):
    # (Vu qu'on décale de 13 lettres, et que l'alphabet a 26 lettres l'algorithme de chiffrement et le même que celui de déchiffrement)
    return encrypt(code)