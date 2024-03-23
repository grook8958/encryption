import shift

# Encrypt Caesar
def encrypt(text, key):
    return shift.encrypt(text, len(key))

# Decrypt Caesar
def decrypt(code, key):
    return shift.decrypt(code, len(key))