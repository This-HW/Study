import re
f = open("test.txt", "r")
lines = f.readlines()
sort = sorted(lines, reverse=True, key=int)
f.close()


f = open("test2.txt", "w")
for i in sort :
   # re.sub(pattern="\n", repl='', string=sort)
    f.writelines(i)
f.close()
