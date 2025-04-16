import time,math
# 1. Timer Decorator
# Write a decorator called timer that measures and prints how long a function takes to execute.

# Task:
# The decorator should print the time it takes for the function to run.
# Use time.time() to measure the time before and after function execution.

# def MeasureTime(func):
#    def wrapper(*args,**kwargs):
#         start = time.time()
#     # print(start)
#         try:
#             func(*args,**kwargs)
#         except:
#             print("Function not found")
#         end = time.time()
#         measureTime = end-start
#         print(f"{func.__name__} took {math.trunc(measureTime)} secs")
#    return wrapper

# # MeasureTime()
# @MeasureTime
# def example_function():
#     time.sleep(2)
#     print('Function has Completed !')

# example_function()



# 2. Uppercase Decorator
# Write a decorator called uppercase_decorator that modifies a function that returns a string, and transforms the result into uppercase.

# Task:
# The decorator should convert the return value of a function to uppercase.
# def uppercase_decorator(func):
#     def wrapper(*args,**kwargs):
#         try:
#             returnValue = func(*args,**kwargs)
#             return returnValue.upper()
#         except:
#             print("Function not Found !")
#     return wrapper



# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Abdulmoiz"))



# 3. Argument Logger Decorator
# Write a decorator called log_arguments that prints out the arguments passed to the decorated function.
# 
# Task:
# The decorator should print the function's name and the arguments passed when the function is called.

# def log_arguments(func):
#     def wrapper(*args,**kwargs):
#         try:
#             print(f"{func.__name__}\n")
#             returnValue = func(*args,**kwargs)
#             print("Positional Arguments",args)
#             print("Keyword Argument",kwargs)
#             return returnValue
#         except:
#             print("Function not Found")
#     return wrapper

# @log_arguments
# def add(a, b):
#     return a + b

# print(add(5, 3))


# 4. Bonus Challenge: Combine Multiple Decorators
# Create a new function with all three decorators applied (i.e., timer, uppercase_decorator, and log_arguments).
# 
# Make sure the output shows the logs for arguments, the time taken for execution, and the uppercase result.

from functools import wraps

def MeasureTime(func):
   @wraps(func)
   def wrapper(*args,**kwargs):
        start = time.time()
    # print(start)
        try:
           timerFunc =  func(*args,**kwargs)
        except Exception as e:
            print("Function not found",e)
            return None
        end = time.time()
        measureTime = end-start
        print(f"{func.__name__} took {math.trunc(measureTime)} secs")
        return timerFunc

   return wrapper

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            returnValue = func(*args,**kwargs)
            return returnValue.upper()
        except Exception as e:
            print("Function not Found !",e)
            return None
    return wrapper

def log_arguments(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            print(f"{func.__name__}\n")
            returnValue = func(*args,**kwargs)
            print("Positional Arguments",args)
            print("Keyword Argument",kwargs)
            return returnValue
        except Exception as e:
            print("Function not Found",e)
            return None
    return wrapper

@MeasureTime
@uppercase_decorator
@log_arguments
def greet_and_add(name, x, y):
    time.sleep(3)
    print(f"Greeting {name} and adding numbers {x} and {y}")
    return f"{name}, result: {x + y}"

print(greet_and_add("Abdulmoiz", 5, 7))