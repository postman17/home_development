class Product:
   def __init__(self, name, volume):
        self.name = name
        self.volume = volume
 
class Container:
    # maxcapacity = 0 # не объявляем в базовом классе, будет абстрактным
 
    def __init__(self):
        self.products = []
        self.capacity = self.maxcapacity
 
    def put(self, product):
        if not isinstance(product, Product):
            raise TypeError('argument must be a Product')
 
        if product.volume > self.capacity:
            raise ValueError('no room left')
 
        self.products.append(product)
        self.capacity -= product.volume
 
class Package(Container):
    maxcapacity = 100
 
class Basket(Container):
    maxcapacity = 200
 
 
while True:
    container_type = input('Выберите тару (kor или pak):\n')
    if container_type in ('kor', 'pak'):
        break
    print('Неверный выбор')
 
container = Basket() if container_type == 'kor' else Package()
 
name = input('Введите товар:\n')
volume = int(input('Введите вместимосить:\n'))
 
try:
    container.put(Product(name, volume))
except ValueError:
    print('Не помещается!')
else:
    print('Товар помещен!')
 
print('Осталось места:', container.capacity)
