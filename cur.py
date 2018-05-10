class ClassName(object):
        def __init__(self, arg, cons):
            self.cons=cons
            self.arg = arg
        def __lt__(self,cons):
            return self.arg < self.cons
        def __gt__(self,cons):
            return self.arg > self.cons
        def __eq__(self,cons):
            return self.arg == self.cons
        
y=5
x=int(input('Ведите число:'))
while x!=y:
    asd=ClassName(x,y)
    if asd>y:
        print('Введенное число больше задуманного!')
    if asd<y:
        print('Введенное число меньше задуманного!')
    
    x=int(input('Ведите число:'))
    asd=ClassName(x,y)
    if asd==y:
        print('Вы угадали!')
