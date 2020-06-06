#####################
### CAESAR CIPHER ###
#####################

def encode(plaintext, key=None, variant="caesar"):
    ciphertext = ""
    if "ROT" in variant: key = 13
    if key == None: raise Exception("You must enter a key for the caesar cipher variant!")
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isupper(): ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower(): ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        elif char.isdigit() and variant == "ROT18": ciphertext += str((int(char) + 5) % 10)
        else: ciphertext += char
    return ciphertext

def decode(ciphertext, key=None, search="", variant="caesar"):
    if "ROT" in variant: return encode(ciphertext, variant=variant)
    if key == None:
        plaintexts = []
        for i in range(1, 25):
            p = encode(ciphertext, -i)
            if search in p: plaintexts.append(p)
        return plaintexts
    return encode(ciphertext, -key)

