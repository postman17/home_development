class korzina:
    def __init__(self,vmes):
        self.vmes=vmes
    def korz(self,tovar):
        self.tovar=tovar

        try:
            if len(self.tovar)>self.vmes:
                raise ValueError
            if len(self.tovar)<=self.vmes:
                print('Товар помещен в корзину!')
        except ValueError:
            print('Непомещается!')

class paket:
    def __init__(self,vmes):
        self.vmes=vmes
    def pak(self,tovar):
        self.tovar=tovar
        
        try:
            if len(self.tovar)>self.vmes:
                raise ValueError
            if len(self.tovar)<=self.vmes:
                print('Товар помещен в корзину!')
        except ValueError:
            print('Непомещается!')

class obsh(korzina):
    def __init__(self,vmes):
        self.vmes=vmes
    def rabota(self,tara,tovar):
        self.tara=tara
        self.tovar=tovar
        if self.tara=='kor':
            a=korzina(self.vmes)
            a.korz(tovar)
        if self.tara=='pak':
            b=paket(self.vmes)
            b.pak(self.tovar)

x=input('Выберите тару(kor или pak):')
y=input('Введите товар:')
z=int(input('Введите вместимосить:'))
asd=obsh(z)
asd.rabota(x,y)
