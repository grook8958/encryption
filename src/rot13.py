import spacing

# Chiffre en ROT13
def encrypt(text):
    return spacing.encrypt(text, 13)

# Déchiffre en ROT13
def decrypt(code):
    return encrypt(code)