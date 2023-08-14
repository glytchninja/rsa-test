from mod import *

publicKey, privateKey = readKeys()

message = input('|--Message\n' + '|--')

encrypted = encrypt(message, publicKey)

print(encrypted)

decrypted = decrypt(encrypted, privateKey)

print(decrypted)