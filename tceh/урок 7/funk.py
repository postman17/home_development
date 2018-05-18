'''
def vag(value):
    print(value%5)

l=[1, 4, 5, 30, 99]

m=map(vag,l)

'''
'''
def vag(value):
    return str(value)
l=[3, 4, 90, -2]
m=map(vag, l)
print(list(m))
'''
'''

l=['some', 1, 'v', 40, '3a', str]

asd=filter(lambda x: type(x)==int, l)
print(list(asd))

'''

from functools import reduce

l=['some', 'other', 'value']

def vag(*value):
    for x in value:
        if type(x)!=str:
            break
        else:
            qwe=len(x)
            print(qwe)

zxc=reduce(vag, l)
print(zxc)
