# Assignment 1: Auto-ID Generator
# 🔹 Create a class decorator @auto_id that:

# Automatically assigns a unique id to every object created.
# Starts from 1 and increments for each new instance.
# Adds an id attribute to each instance.
# 🔸 Apply it to a class User(name, email).

# def auto_id(cls):
#     cls._id_counter =0
#     original_init = cls.__init__
#     def newInit(self,*args,**kwargs):
#         cls._id_counter += 1
#         self.id = cls._id_counter
#         original_init(self,*args,**kwargs)
#     cls.__init__ = newInit

#     return cls

# @auto_id
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

# user1 = User("Sam","sam@gmail.com")
# print(user1.__dict__)
# user2 = User("Tom","tom@gmail.com")
# print(user2.__dict__)



# Assignment 2: Limit Instances
# 🔹 Create a decorator @limit_instances(max_count) that:

# Prevents creating more than max_count objects of a class.
# If limit is reached, print "Limit reached!" and do not create a new instance.
# def limit_instances(max_count):
#     def decorator(cls):
#         cls.limit_instance = 1
#         original_init = cls.__init__
#         def newInit(self,*args,**kwargs):
#             if cls.limit_instance>max_count:
#                 print("Limit reached!")
#                 return 
#             else:
#                 print(f"Session {cls.limit_instance} created")
#                 cls.limit_instance +=1
#                 original_init(self,*args,**kwargs)
#         cls.__init__ = newInit
#         return cls
#     return decorator

# @limit_instances(3)
# class Session:
#     # def __init__(self):
#         # print("Session initialized.")
#         pass

# ses1 = Session()
# ses2 = Session()
# ses3 = Session()
# ses4 = Session()
# ses5 = Session()

#  Assignment 3: Automatically Register Classes
# 🎯 Goal: Use a decorator to track every class created using a global list REGISTERED_CLASSES.

# registerClass = []
# def register_class(cls):
#     registerClass.append(cls.__name__)
#     # original_init = cls.__init__
#     # def newInit(self,*args,**kwargs):
#     #     original_init(self,*args,**kwargs)
#     # cls.__init__ = newInit
#     return cls


# @register_class
# class Book:
#     pass

# @register_class
# class Article:
#     pass

# print(registerClass)


# Assignment 4: Attach a Logger to Every Class
# 🔹 Write a decorator @attach_logger that:

# Adds a method log(message) to the class.

# When log() is called, it prints:
# [<ClassName>] <message>
# 🔸 Use it on class Order

# def attachlogger(cls):
#     original_init = cls.__init__
#     def newInit(self,*args,**kwargs):
#         original_init(self,*args,**kwargs)
#     def log(self,message):
#         return f"{cls.__name__} {message}"
#     cls.__init__ = newInit
#     cls.log = log
#     return cls

# @attachlogger
# class Order:
#     def __init__(self):
#         pass

# order1 = Order()
# print(order1.log("Order Placed"))
    

# ✅ Assignment 4: Restrict Instantiation (Singleton Pattern)
# 🎯 Goal: Allow only one instance of a class to be created. If already created, return the old one.
# def singletons(cls):
#     cls.instanceCount = 0
#     original_init = cls.__init__
#     if cls.instanceCount>1:
#         return cls
#     else:
#         def newInit(self,*args,**kwargs):
#             cls.instanceCount +=1
#             original_init(self,*args,**kwargs)
#         cls.__init__ = newInit
#         return cls


def singleton(cls):
    _instance = None  # Store the single instance

    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = cls(*args, **kwargs)
        return _instance

    return wrapper

@singleton
class AppSettings:
    def __init__(self):
        print("Initializing settings...")

s1 = AppSettings()
s2 = AppSettings()
print(s1 is s2)        
        




