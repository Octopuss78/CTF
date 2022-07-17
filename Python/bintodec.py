import sys

sbin = sys.argv[1]

i = len(sbin)-1
res = 0
e = 0

while i >= 0:
    if sbin[i] != " ":
       res += (int(sbin[i]) * (2 ** e))
       e+=1
    i-=1
print(res)