######################
### FORENSICS TEST ###
######################

from foren import audsteg, imgsteg

a = audsteg.get_lsb("example.wav")
print("Original Audio LSBs: " + a[:100] + "... (truncated)")
audsteg.enc_lsb("example.wav", "Hi there! I love audio steganography. Don't you?", "example_encoded.wav")
a = audsteg.get_lsb("example_encoded.wav")
print("Encoded Audio LSBs: " + a[:100] + "... (truncated)")

i = imgsteg.get_lsb("example.png")
print("Original Image LSBs: " + i[:100] + "... (truncated)")
imgsteg.encode_lsb("example.png", "Magic is real. This is a fact!", "example_encoded.png")
i = imgsteg.get_lsb("example_encoded.png")
print("Encode Image LSBs: " + i[:100] + "... (truncated)")
