###################
### CRYPTO TEST ###
###################

from crypto import caesar, vigenere, a1z26

c = caesar.encode("flag{m4gIc_i5_r3al}", variant="ROT18")
print("ROT18 encode: " + c)
print("ROT18 decode: " + caesar.decode(c, variant="ROT18"))

v = vigenere.encode("flag{m4gIc_i5_r3al}", "ctf")
print("Vigenere encode: " + v)
print("Vigenere decode w/ key: " + vigenere.decode(v, key="ctf")[0])

v = vigenere.encode("Hello there! My name is Bob Smith! I enjoy playing soccer and reading books! However, "
                    "my favorite thing in the world is to watch a puffin. Puffins are the best animals that can be "
                    "seen on the face of the Earth! You can see many puffins on the island of Iceland.",
                    key="puffins")
print("Long vigenere encode: " + v)
vd = vigenere.decode(v, maxkeysize=10)
print("Long vigenere decode w/o key: " + vd[0] + "\n\tKey: " + vd[1])

a = "thisisatestothercharacterswillcomesoon"
a2 = a1z26.encode(a)
print(a2)
print(a1z26.decode(a2, '-'))
