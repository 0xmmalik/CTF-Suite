#######################
### VIGENERE CIPHER ###
#######################

import itertools

ENG_FREQ = [0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357, 0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028, 0.0164, 0.0004]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encode(plaintext, key):
    ciphertext = ""
    x = 0
    for i in range(len(plaintext)):
        keychar = key[x % len(key)]
        char = plaintext[i]
        if char.isupper():
            ciphertext += chr((ord(char) + ord(keychar) - 97 - 65) % 26 + 65)
            x += 1
        elif char.islower():
            ciphertext += chr((ord(char) + ord(keychar) - 97 - 97) % 26 + 97)
            x += 1
        else: ciphertext += char
    return ciphertext

def freq_diff(text):
    text = [t for t in text.lower() if t.islower()]
    freq = [0] * 26
    total = float(len(text))
    for let in text: freq[ord(let) - ord('a')] += 1
    return sum(abs(f / total - E) for f, E in zip(freq, ENG_FREQ))

def decode_with_key(ciphertext, key):
    plaintext = ""
    x = 0
    for i in range(len(ciphertext)):
        keychar = key[x % len(key)]
        char = ciphertext[i]
        if char.isupper():
            plaintext += chr((ord(char) - ord(keychar) + 97 - 65) % 26 + 65)
            x += 1
        elif char.islower():
            plaintext += chr((ord(char) - ord(keychar) + 97 - 97) % 26 + 97)
            x += 1
        else: plaintext += char
    return plaintext

def decode(ciphertext, key=None, minkeysize=3, maxkeysize=25):
    if key == None:
        poss = []
        letters = [let for let in ciphertext if let.islower() or let.isupper()]
        for keylen in range(minkeysize, maxkeysize):
            k = [None] * keylen
            for i in range(keylen):
                mod_letters = "".join(itertools.islice(letters, i, None, keylen))
                shifts = []
                for let in ALPHABET: shifts.append((freq_diff(decode_with_key(mod_letters, let)), let))
                k[i] = min(shifts, key=lambda x: x[0])[1]
            poss.append("".join(k))
        poss.sort(key=lambda key: freq_diff(decode_with_key(ciphertext, key)))
        key = poss[0]
    return decode_with_key(ciphertext, key)
