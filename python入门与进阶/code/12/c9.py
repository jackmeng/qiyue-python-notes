import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(name):
    print('This is a function' + name)

@decorator
def f2(name,age):
    print('This is a function '+name + 'age' + str(age))

@decorator
def f3(name,age,**kw):
    print('This is a function '+name + 'age' + str(age))
    print(kw)

f1('f1')
f2('f2',10)
f3('f3',12,a=1,b=2)

