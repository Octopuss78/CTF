import sys


s = str(sys.argv[1])

#hex to bin
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

#bin ot ascii txt
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


print(res)
