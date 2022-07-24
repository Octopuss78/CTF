from bases import *

def to_nbits(s,b):

    #Return res the string shortened to b chars and tmp the rest of the old string

    res = ""
    tmp = ""
    a = False
    n = 0
    for i in range(0,len(s)):
        if i < b:
            res += s[i]
        else:
            tmp += s[i]
            if i != len(s)-1 and s[i] == " ":
                res += " "
        n+=1
    if i < b:
        for k in range (0, b+1-n):
            res = '0' + res
    return res, tmp


def uu_decode(s):
    res = ""
    tmp = ""
    for i in range(0, len(s)):
        a = ord(s[i])
        z = to_nbits(dec_to_bin(a),8)
        print(z)
        nb = 2 + ((len(tmp) % 4) * 2)
        #if nb == 8:
        #   nb = 2
        x,r = to_nbits(s,(len(tmp)+2))
        print(x)
        y = tmp + x
        tmp = r
        b = bin_to_dec(y)
        res += chr(int(b) + 32)

    return res