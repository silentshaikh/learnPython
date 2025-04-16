# ✅ Assignment 1: Simple Function Decorator
# 🎯 Goal: Create a decorator that simply prints a message before and after the execution of a function.
# def simpleDecorator(func):
#     def wrapper():
#         print("Before Function Execution")
#         func()
#         print("After Function Execution")
#     print(wrapper)
#     return wrapper

# @simpleDecorator
# def greet():
#     print("Hello World")
# greet()


# ✅ Assignment 2: Decorator with Arguments
# 🎯 Goal: Create a decorator that accepts arguments. The decorator should log the arguments passed to the function.
# def log_argument(func):
#     def wrapper(*args,**kwargs):
#         print(f"Arguments : {args} {kwargs}")
#         return func(*args,**kwargs)
        
#     return wrapper


# @log_argument
# def showArgument(a,b):
#     return a+b
# print(showArgument(5,5))


# ✅ Assignment 3: Function Return Value Decorator
# 🎯 Goal: Create a decorator that modifies the return value of a function. For example, double the return value of a function.
# def modifyReturnValue(func):
#     def wrapper(*args,**kwargs):
#       return  func(*args,**kwargs) ** 2
#     return wrapper

# @modifyReturnValue
# def returnValue(x):
#    return x*x
# print(returnValue(4))
         

# ✅ Assignment 4: Function Timing Decorator
# 🎯 Goal: Create a decorator that measures the time taken to execute a function and prints the execution time.
# import time,math
# def MeasureTime(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         containSec = f"They took {math.trunc(end-start)} seconds"
#         print(containSec)
#     return wrapper

# @MeasureTime
# def callFunc():
#     time.sleep(2)

# callFunc()


# ✅ Assignment 5: Class Decorator with Instance Count
# 🎯 Goal: Create a class decorator count_instances that tracks how many instances of a class have been created.
# def count_instance(cls):
#     cls.instance_count = 0
#     original_init = cls.__init__
#     def newInit(self,*args,**kwargs):
#         cls.instance_count += 1
#         print(f"{cls.__name__} has {cls.instance_count} Instance")
#         original_init(self,*args,**kwargs)
#     cls.__init__ = newInit
#     return cls

# @count_instance
# class Book:
#     def __init__(self):
#         pass

# book1 = Book()
# book2 = Book()


# ✅ Assignment 6: Add Timestamp to Class Instances
# 🎯 Goal: Write a class decorator that adds a created_at timestamp to every instance of a class.
# from datetime import datetime
# def add_timestamp(cls):
#     cls.created_at = None
#     original_init = cls.__init__
#     def newInit(self,*args,**kwargs):
#         cls.created_at = datetime.now()
#         self.createdAt = cls.created_at
#         original_init(self,*args,**kwargs)
#     cls.__init__ = newInit
#     return cls

# @add_timestamp
# class Shop:
#     def __init__(self,name):
#         self.name = name

# shop = Shop("BWMCA")
# print(shop.name)
# print(shop.createdAt)


# ✅ Assignment 7: Decorator to Add Method to Class Dynamically
# 🎯 Goal: Create a decorator that adds a method describe() dynamically to any class.
def addMethod(cls):
    original_init = cls.__init__
    def describe(self):
        return f"Product {self.product} with only {self.price} dollar"
        
    def newInit(self,*args,**kwargs):
        self.describe = describe
        original_init(self,*args,**kwargs)
    cls.__init__ = newInit
    return cls

@addMethod
class Product:
    def __init__(self,product,price):
        self.product = product
        self.price = price

product1 = Product("Apple",3)
print(product1.describe(product1))


# ✅ Assignment 8: Decorator for Caching Results
# 🎯 Goal: Write a decorator cache_result that caches the result of a function so that if the function is called again with the same parameters, it returns the cached result instead of recomputing it.
# def cache_result(func):
#     result = {}
#     def wrapper(*args):
#         if args in result:
#             return result[args]
#         funcResult = func(*args)
#         result[args] = funcResult
#         return result
#     return wrapper

# @cache_result
# def myResult(a,b):
#     return a+b

# print(myResult(3,5))
# print(myResult(3,5))
# print(myResult(3,4))
# print(myResult(3,4))


# ✅ Assignment 9: Singleton Class Decorator
# 🎯 Goal: Write a singleton class decorator that ensures only one instance of a class can exist.
# def singleton(cls):
#     instances = None
#     def wrapper(*args,**kwargs):
#         nonlocal instances
#         if instances is None:
#             instances = cls(*args,**kwargs)
#         return instances
#     return wrapper

# @singleton
# class Setting:
#     def __init__(self,name):
#         self.name = name

# set1 = Setting("Lorem")
# set2 = Setting("Ipsum")
# print(set1 is set2)
# print(set1.__dict__)
# print(set2.__dict__)


# ✅ Assignment 10: Decorator for User Authentication (Advanced)
# 🎯 Goal: Create a decorator requires_authentication that checks if a user is authenticated before proceeding with the function. If not, it raises an exception.

# def requires_authentication(func):
#     def wrapper(user,*args,**kwargs):
#         if not user.get("authenticated",False):
#             raise PermissionError('User is not authenticated!')
#         else:
#             return func(user,*args,**kwargs)
#     return wrapper

# user_authenticated = {"name": "Abdulmoiz", "authenticated": True}
# user_unauthenticated = {"name": "Ali", "authenticated": False}
# @requires_authentication
# def viewUser(user):
#     print(f"Viewing the User : {user["name"]}")

# viewUser(user_unauthenticated)


# 💡 Bonus Challenge (Advanced): Decorator for Rate Limiting
# 🎯 Goal: Write a rate_limit decorator that limits the number of times a function can be called within a certain time period.
import time

def rate_limit(func):
    last_called = [0]
    def wrapper(*args,**kwargs):
        if time.time()-last_called[0] < 3:
            raise Exception("Rate limit exceeded! Try again later.")
        last_called[0] = time.time()
        return func(*args,**kwargs)
    return wrapper

@rate_limit
def fetch_data():
    print("Fetching Data")

fetch_data()
fetch_data()
fetch_data()
