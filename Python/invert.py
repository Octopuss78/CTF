import sys


s = sys.argv[2]
j = 0
res = ""
x = int(sys.argv[1])
n=x-1

while j < len(s)-x:
    if n >= 0:
        res+=s[j+n]
        n-=1
    else:
        n=x-1
        j+=4
print(res)