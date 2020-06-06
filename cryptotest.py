###################
### CRYPTO TEST ###
###################

from crypto import caesar, vigenere

c = caesar.encode("flag{m4gIc_i5_r3al}", variant="ROT18")
print(c)
print("ROT18 decode: " + caesar.decode(c, variant="ROT18"))

v = vigenere.encode("flag{m4gIc_i5_r3al}", "ctf")
print(v)
