import sys

nb = sys.argv[1]
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

print(res)