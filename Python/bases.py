import sys

#s = str(sys.argv[1])

############# CLASSIC BASE CHANGES##############

def hex_to_bin(s):
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
    sbin = sbin.replace(" ", "")
    i = len(sbin)-1
    res = 0
    e = 0
    while i >= 0:
        if sbin[i] != " ":
            res += (int(sbin[i]) * (2 ** e))
            e+=1
            i-=1
    return res
    #print(res)

def bin_to_ascii(sbin):
    sbin = sbin.replace(" ", "")
    i = 0
    res = ""

    while i < len(sbin):
        tmp = ""
        for j in range(0,8):
            if i+j < len(sbin):
                tmp += sbin[i+j]
        x = int(tmp, 2)
        res += chr(x)
        i+=8
    return res
    #print(res)

def nb_to_ascii(nb):
    tmp = ""
    res = ""

    for i in range(0,len(nb)):
        if nb[i] != " ":
            if nb[i] == '{' or nb[i] == '}':
                res+=nb[i]
                tmp = ""
            else:
                tmp += nb[i]
            print(res)
        else:
            if tmp != "":
                print(tmp)
                res += chr(int(tmp)+96)
                tmp = ""
        return res
    #print(res)

##############################################

############### COMBINATION ##################

def hex_to_txt(s):
    sx = hex_to_bin(s)
    return bin_to_ascii(sx)


##############################################