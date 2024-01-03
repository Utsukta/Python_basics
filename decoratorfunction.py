# import logging

# def log_function_call(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result=func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_func(a,b):
#     return a+b

# my_func(2,3)


# Without passing arguments
def greetfunc(func):
    def Mfx():
        print("Good morning")
        func()
        print("Thank you")
    return Mfx
    
@greetfunc
def hello():
    print("hello world")

hello()


#With passing arguments
def greetfunc(func):
    def Mfx(*args, **kwargs):
        print("Good morning")
        func(*args, **kwargs)
        print("Thank you")
    return Mfx


@greetfunc
def info(n,a,b):
    print(f"My name is {n} and age is {a} and I live in {b}")

# greetfunc(info)("Utsukta",12)
info("Utsukta",10,"lalitpur")