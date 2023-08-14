import rsa


def getKeys(bits):
    return rsa.newkeys(bits)


def saveKeys(publicKey, privateKey):
    with open("public.pem", "wb") as f:
        f.write(publicKey.save_pkcs1("PEM"))
    with open("private.pem", "wb") as f:
        f.write(privateKey.save_pkcs1("PEM"))


def readKeys():
    with open("public.pem", "rb") as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
    with open("private.pem", "rb") as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    return publicKey, privateKey


def encrypt(message, publicKey):
    encrypted = rsa.encrypt(message.encode(), publicKey)
    return encrypted


def decrypt(message, privateKey):
    try:
        decrypted = rsa.decrypt(message, privateKey)
        return decrypted.decode()
    except Exception:
        return "Error, decryption failed"