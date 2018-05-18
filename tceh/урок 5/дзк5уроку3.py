class Animal:
    animallist={}
    def dobav(self,name,flag):
        self.name=name
        self.flag=flag
        
        if self.flag=='poisonous' or self.flag=='predator' or self.flag=='nope':
            self.animallist[self.name]=self.flag
        else:
            print('неверный флаг!')

    def list(self):
        return print(self.animallist)

class Human(Animal):
    def is_dangerous(self,animal):
        self.animal=animal
        for a,b in self.animallist.items():
            if a==self.animal:
                if b=='poisonous' or b=='predator':
                    print('Животное {} опасно для человека, оно {}'.format(animal,b))
                if b=='nope':
                    print('Животное {} не опасно для человека!'.format(animal))



x=Animal()
x.dobav('Гадюка','poisonous')
c=Animal()
c.dobav('Кот','nope')
asd=Animal()
asd.dobav('Собака','nope')
asd.list()


zxc=Human()
zxc.is_dangerous('Кот')
