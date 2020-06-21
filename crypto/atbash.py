#####################
### ATBASH CIPHER ###
#####################

from collections import Counter

ENG_FREQ = [0.0749, 0.0129, 0.0354, 0.0362, 0.14, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357, 0.0339,
            0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.03, 0.0116, 0.0169, 0.0028, 0.0164, 0.0004]
ENG_FREQ.sort()

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encode(plaintext, alphabet="zyxwvutsrqponmlkjihgfedcba"):
    upper = alphabet.upper()
    lower = alphabet.lower()
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isupper():
            ciphertext += upper[UPPER_ALPHABET.index(char)]
        elif char.islower():
            ciphertext += lower[LOWER_ALPHABET.index(char)]
        else:
            ciphertext += char
    return ciphertext


def decode(ciphertext, alphabet=None):
    # TODO: implement
    if alphabet is None:
        text = [t for t in ciphertext.lower() if t.islower()]
        total = float(len(text))
        ct = Counter(ciphertext.lower())
        alphabet = ""
        # for let, _ in ct.most_common():
    # for i in range(len(freqs)): alphabet += ENG_FREQ[
