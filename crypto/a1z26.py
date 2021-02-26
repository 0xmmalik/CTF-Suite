####################
### A1Z26 CIPHER ###
####################

ALPHA = "abcdefghijklmnopqrstuvwxyz"


def encode(plaintext, delimiter='-'):
    """for alpha characters only"""
    ciphertext = ""
    plaintext = plaintext.lower()
    for i in range(len(plaintext)):
        ciphertext += str(ALPHA.index(plaintext[i]) + 1) + delimiter
    ciphertext = ciphertext[:-1]
    return ciphertext


def decode(ciphertext, delimiter):
    """for alpha characters only"""
    plaintext = ""
    ciphertext = ciphertext.split(delimiter)
    for num in ciphertext:
        plaintext += ALPHA[int(num) - 1]
    return plaintext
