import sys
from bases import *

##### bases.py and 2xPadDecrypt must be in the same directory #####

def check_dec(nbe):
    if nbe == 1 or nbe == 2:
        print("Now choose the conversion method:", '\n',
                "(1): Ascii/text", '\n',
                "(2): Decimal", '\n')
    else:
        print("Now choose the conversion method:", '\n',
                "(1): Ascii/text")
    nbd = int(input(": "))
    nbd = int(nbd)
    print("")
    if nbd <= 0 or nbd > 3:
        raise ValueError("invalid input")
    return nbd



def decode():
    print("Current format:", '\n',
            "(1): Binary", '\n',
            "(2): Hexadecimal", '\n',
            "(3): 2xPad", '\n')
    nbe = input(": ")

    print("")

    nbe = int(nbe)

    if int(nbe) <= 0 or int(nbe) > 4:
        raise ValueError("invalid input")
    
    print("Enter the string to convert",'\n')
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

            return nb_to_ascii(s)


