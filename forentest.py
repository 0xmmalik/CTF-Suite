######################
### FORENSICS TEST ###
######################

from foren import audsteg

a = audsteg.get_lsb("example.wav")
print("Original Audio LSBs: " + a[:100] + "... (truncated)")
audsteg.enc_lsb("example.wav", "Hi there! I love audio steganography. Don't you?", "example_encoded.wav")
a = audsteg.get_lsb("example_encoded.wav")
print("Encoded Audio LSBs: " + a[:100] + "... (truncated)")
