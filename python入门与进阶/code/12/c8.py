import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def f1():
    print('This is a function')

f = decorator(f1)
f()

@decorator
def f2():
    print('This is a function f2')
    
f2()