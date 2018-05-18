class figure:
   def __init__(self,*args):
      self.value=args
   def kvadrat(self):
      self.kvad=tuple(self.value**2,self.value*4)
      return tuple(self.value**2,self.value*4)
   def pryam(self,*args):
      self.args=args
      plosh=self.args[0]*self.args[1]
      perim=(self.args[0]*2)+(self.args[1]*2)         
      return plosh,perim
   def treug(self,*args):
      self.args=args
      perim=self.args[0]+self.args[1]+self.args[2]
      p=perim/2
      plosh=(p*(p-self.args[0])*(p-self.args[1])*(p-self.args[2]))**0.5
      return plosh, perim
   def mnogo(self,*args):
      self.args=args
      x=0
      for i in args:
         x+=i
      perim=x
      return 0,perim

print('Если 1 число - квадрат')
print('Если 2 числа - прямоугольник')
print('Если 3 числа - треугольник')
print('Если 4 числа - многоугольник')
x=input('Ведите значения через пробел:')
zxc=''
for c in x:
   if c!=' ':
      zxc+=c
sdf=tuple(zxc)
if len(sdf)==1:
   asd=figure(zxc)
   asd.kvadrat
   print(asd)
if len(sdf)==2:
   asd=figure()
   print(asd.pryam)
if len(sdf)==3:
   asd=figure()
   print(asd.treug)
if len(sdf)>=4:
   asd=figure()
   print(asd.mnogo)
