class Person():
    def __init__(self,age,name):
        self.age=age
        self.name=name
        spisok=[]
    def know(self,*person):
        self.person=[n for n in person]
    def is_known(self,person):
        if person in self.person:
            print('Есть такой человек!')
        else:
            print('Такого человека нет в списке!')

x=Person(30,'Константин')
x.know('peter','ivan','maria')
x.is_known('nana')
