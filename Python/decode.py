import sys
from bases import *
from uu import *

##### bases.py and 2xPadDecrypt must be in the same directory #####

def check_dec(nbe):
    if nbe == 1 or nbe == 2 or nbe == 5 or nbe == 4:
        print("Now choose the conversion method:", '\n',
                "(1): Ascii/text", '\n',
                "(2): Decimal", '\n')
    elif nbe != 6:
        print("Now choose the conversion method:", '\n',
                "(1): Ascii/text")
    if nbe != 6:
        nbd = int(input(": "))
        nbd = int(nbd)
        print("")
        if nbd <= 0 or nbd > 2:
            raise ValueError("invalid input")
        return nbd
    else:
        return None



def decode():
    print("Current format:", '\n',
            "(1): Binary", '\n',
            "(2): Hexadecimal", '\n',
            "(3): 2xPad", '\n',
            "(4): Decimal", '\n',
            "(5): Octal", '\n',)
            #"(6): UU-Encoding",'\n')
    nbe = input(": ")

    print("")

    nbe = int(nbe)

    if int(nbe) <= 0 or int(nbe) > 6:
        raise ValueError("invalid input")
    
    print("Enter the string to convert")
    s = input(": ")
    print("")


    nbd = check_dec(nbe)
    if nbe == 1:
        if nbd == 1:
            return bin_to_ascii(s)
        else:
            return bin_to_dec(s)
    elif nbe == 2:
        if nbd == 2:
            return hex_to_bin(s)
        elif nbd == 1:
            return hex_to_txt(s)
        else:
            x = str(hex_to_bin(s))
            return bin_to_dec(x)
    elif nbe == 3:
        if nbd != 1:
            raise ValueError("invalid input")
        else:
                print("Enter the encrypted key convert", '\n', '\n')
                encryptedkey = input(": ")
                print("")
                from twotimespad import two_times_pad
                return two_times_pad(encryptedkey, s)
    elif nbe == 4:
        if nbd != 1:
            raise ValueError("invalid input")
        else:
            return dec_to_ascii(s)
    elif nbe == 5:
        """if nbd == 2:
            return oct_to_dec(s)"""
        if nbd == 1:
            return oct_to_txt(s)
        elif nbd == 2:
            return oct_to_dec(s)
        else:
            raise ValueError("invalid input")
    """elif nbe == 6:
        return uu_decode(s)"""


