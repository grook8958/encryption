import shift

# Encrypt Caesar
def encrypt(text):
    return shift.encrypt(text, 3)

# Decrypt Caesar
def decrypt(code):
    return shift.decrypt(code, 3)