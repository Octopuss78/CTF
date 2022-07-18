import sys

#s = str(sys.argv[1])

############# CLASSIC BASE CHANGES##############

def hex_to_bin(s):
    s = str(s)
    s = s.replace(" ", "")
    i=0 
    j=0 
    sbin = ""

    while i < len(s):
        if s[i] == 'f' or s[i] == 'F':
            sbin += "1111"
        elif s[i] == 'e'or s[i] == 'E':
            sbin += "1110"
        elif s[i] == 'd' or s[i] == 'D':
            sbin += "1101"
        elif s[i] == 'c' or s[i] == 'C':
            sbin += "1100"
        elif s[i] == 'b' or s[i] == 'B':
            sbin += "1011"
        elif s[i] == 'a' or s[i] == s[i] == 'A':
            sbin += "1010"
        else:
            tmp = int(s[i])
            y = ""
            for k in range(0,4):
                x = int(tmp) % 2
                y = str(x) + y
                tmp = str(int(tmp) // 2)
            sbin += y
        i+=1
    return sbin

def bin_to_dec(sbin):
    sbin = str(sbin)
    i = len(sbin)-1
    res = ""
    x= 0
    e = 0
    while i >= 0:
        if sbin[i] != " " and i > 0:
            x += int(sbin[i]) * (2 ** e)
            e+=1
        else:
            res = str(x) + res
            x = 0
            e = 0
            if i > 0:
                res = " " + res 
        i-=1
    return res
    #print(res)

def bin_to_ascii(sbin):
    sbin = str(sbin)
    sbin = sbin.replace(" ", "")
    i = 0
    res = ""

    while i < len(sbin):
        tmp = ""
        for j in range(0,8):
            if i+j < len(sbin):
                tmp += sbin[i+j]
        #x = int(tmp, 2)
        x = int(bin_to_dec(tmp))
        res += chr(x)
        i+=8
    return res
    #print(res)

def dec_to_ascii(nb):
    tmp = ""
    res = ""
    nb = str(nb)
    for i in range(0,len(nb)):
        if nb[i] != " ":
            tmp += nb[i]
            if i == len(nb)-1:
                res += chr(int(tmp))
                tmp = ""
        else:
            res += chr(int(tmp))
            tmp = ""
    return res

def oct_to_bin(s):
    res = ""
    i = 0
    while i < len(s):
        y = ""
        if s[i] != " ":
            tmp = str(s[i])
            for k in range(0,3):
                if int(s[i]) < 8:
                    x = int(tmp) % 2
                    y = str(x) + y
                    tmp = str(int(tmp) // 2)
                else:
                    raise ValueError("Number must be below 8 in octal")
            res += y
        else:
                res += y
                res+= " "
        i+=1
    return res
##############################################

############### COMBINATION ##################

def hex_to_txt(s):
    sx = hex_to_bin(s)
    return bin_to_ascii(sx)

def oct_to_txt(s):
    sy = oct_to_bin(s)
    sz = bin_to_dec(sy)
    return dec_to_ascii(sz)

"""def oct_to_dec(s):
    z = oct_to_bin(s)
    print(z)
    return bin_to_dec(s)"""

##############################################