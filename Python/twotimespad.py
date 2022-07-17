import sys

#encryptedkey = sys.argv[1]
#strtodecode = sys.argv[2]

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def two_times_pad(encryptedkey, strtodecode):
    enc_flag = bytes.fromhex(strtodecode)
    enc_text = bytes.fromhex(encryptedkey) 

    dec_text = b'A'*32 # String of 32 times 'A' in binary --> 32 is our (length/2)

    key = byte_xor(enc_text, dec_text) # We kinda remove (XOR) the 32 'A' from the encrypted key

    return(byte_xor(enc_flag, key).decode()) #We use the XOR process using our actual key applied on the encryoted string to decode

