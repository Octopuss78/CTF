import sys

sbin = sys.argv[1]
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
print(res)