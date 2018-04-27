# проверка github
# third commit проверка
with open('datas.txt') as inf:
    qwe = inf.readline().strip()
print (qwe)
b=0
c=0
f=0
qwer=open('text.txt', 'w')
for x in range(0, len(qwe)):
    

    if x<(len(qwe)-2):
        b=qwe[x]
        c=qwe[x+1]
        d=qwe[x+2]
        if b.isalpha() and c.isdigit() and d.isalpha():
            qwer.write(qwe[x])
            print (qwe[x]*int(c), end="")
        elif b.isalpha() and c.isdigit() and d.isdigit():
            qwer.write(qwe[x]*int(c+d))
            print (qwe[x]*int(c+d),end="")
        else:
            continue
    elif x==(len(qwe)-1):
        break
qwer.close()
