'''
#Время выполнения функции

import time

def my_timer(f):
    def tmp(*args, **kwargs):
        start_time=time.time()
        result=f(*args, **kwargs)
        delta_time=time.time() - start_time
        print ('Время выполнения функции {}' .format(delta_time))
        return result

    return tmp


@my_timer
def my_sum(x, y, z):
    return x + y + z

print (my_sum(4, 5, 7))


#С записью в файл

def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('my_file', 'a') as f:
            f.write(
                'function name: {func_name} with result = {result}. Start at {start_time}\n\n'.format(
                    func_name=func.__name__, result=result, start_time=time.ctime(time.time()))
                )
            f.close()
            return result
    return wrapper

@my_timer
@logging
def my_sum(x, y, z):
    return x + y + z

print(my_sum(4, 5, 7))
'''

import time

def logger(func):
    print('Create decorator!')
    def wrapper(args):
        print('Function start working...')
        des=func(args)
        print('Function stop working!')
        return des
    return wrapper

def bug_decor(func):
    def wrapper(args):
        try:
            
            return func(args)
            
        except ValueError:
            print('Error value, try digit number')

        
    return wrapper

def decor(func):
    def wrapper(args):
        start_time=time.time()
        rez=func(args)
        vrem=time.time()-start_time
        print('Time to work function: {}'.format(vrem))
        return rez
    return wrapper

@decor
@logger
@bug_decor

def vag(args):
    summary=0
    for x in range(int(args)):
        asd=int(input('Input number: '))
        summary+=asd
    return 'Sum input numbers: ' + str(summary)


zxc=input("Input number for counter: ")

print(vag(zxc))






