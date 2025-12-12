import time

# 1
def decorator(func):
    def wrapper(*args, **kwargs):
        if args or kwargs:
            print(f"Received arguments: ", args, kwargs)
        else:
            print ("No arguments received")
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    print(f"The sum is: {a + b}")

@decorator
def say_hello():
    print("hello world!")

print("Test 1")
add(10, 5)

print("Test 2")
say_hello()

# 2

def t_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.ctime()
        print(f"Func start time:", start)
        result = func(*args, **kwargs)
        end = time.ctime()
        print(f"Func end time:", end)
        return result

    return wrapper

@t_decorator
def some_func():
    print("Doing work...")

some_func()

# 3

def decorator2(func):
    def wrapper(*args, **kwargs):
        count_args = len(args)
        count_kwargs = len(kwargs)
        result = count_args + count_kwargs
        if result >= 1:
            return func(*args, **kwargs)
        else:
            print("No arguments passed. Not executing the function.")
    return wrapper

@decorator2
def hello(n):
    print(n)

@decorator2
def error():
    print("Error")

hello("ss")

error()