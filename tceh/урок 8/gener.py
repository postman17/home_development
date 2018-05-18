#задание 1
'''
import random
def gen():
    while True:
        yield random.randrange(1,100)

x=gen()
print(next(x))
'''

'''
#задание 2

def gen(y):
    while True:
        asd=0
        l=[]
        while asd<y:
            l.append(asd)
            asd+=1
        yield l


x=gen(10)
print(next(x))
'''

'''
#задание 3

def gen(func, spis):
    while True:
        asd=[]
        if func=='int':
            for x in spis:
                asd.append(int(x))
            yield asd
l=['1','2','3','4','5']
x=gen('int',l)
print(next(x))
'''

'''
#задание 4

def gen(spis):
    while True:
        d={}
        asd=0
        for x in spis:
            d.update({asd:x})
            asd+=1
        yield d
        
l=['1','2','3','4','5']
x=gen(l)
print(next(x))
'''

#задание 5

class gen():
    def __init__(self,*args):
        for x in args:
            self.x=x
        for
