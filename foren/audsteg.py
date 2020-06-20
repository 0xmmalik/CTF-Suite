###########################
### AUDIO STEGANOGRAPHY ###
###########################

import wave


def get_lsb(filepath):
    wv = wave.open(filepath, mode="rb")
    wv_bytes = bytearray(list(wv.readframes(wv.getnframes())))
    wv.close()
    wv_lsb = [wv_bytes[i] & 1 for i in range(len(wv_bytes))]

    extracted_bin = ''.join([str(x) for x in wv_lsb])
    return ''.join(chr(int(extracted_bin[i:i + 8], 2)) for i in range(0, len(extracted_bin), 8))


def enc_lsb(filepath, message, outputfile):
    wv = wave.open(filepath, mode="rb")
    wv_bytes = bytearray(list(wv.readframes(wv.getnframes())))
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))
    for i, bit in enumerate(bits):
        wv_bytes[i] = (wv_bytes[i] & 254) | bit
    wv_mod = bytes(wv_bytes)
    with wave.open(outputfile, "wb") as new_wv:
        new_wv.setparams(wv.getparams())
        new_wv.writeframes(wv_mod)
    wv.close()
    return 0
