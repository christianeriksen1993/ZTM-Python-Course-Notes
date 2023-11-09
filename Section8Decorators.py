# 152. Decorators
"""def hello(func):
    func()

def greet():
    print("Still here!") 

a = hello(greet)
print(a) # Doesn't need to use brackets when calling greet because the hello function calls the func parameter.

# Higher order function HOC
# A function that accepts another function inside, like hello above.
# A function that returns another function. 
def greet2():
    def func():
        return 5
    return func
# Examples are map(), filter(), reduce()"""

"""# 154. Decorators 2, 153. Decorators 3

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("*********")
    return wrap_func

@my_decorator
def hello(greeting, emoji=":("):
    print(greeting, emoji)

hello("Hi")"""

"""# 156. Why do we need decorators
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()"""

# 157. Exercise @authenticated

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"] == True:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)