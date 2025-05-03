import datetime,inspect,json
# ✅ Part 1: Understand type as a Metaclass
# Task 1:
# Use the type() function to create a class manually.

# def greet(self):
#     print("Bow Bow !")

# MetaType = type("Dog",(object,),{
#     "name":"German Sphered",
#     "greet": greet
# })



# the_dog = MetaType()
# the_dog.greet()



# ✅ Part 2: Inspect What Python Does Internally
# Task 2:
# Write a normal class using class, and inspect what type is doing behind the scenes.


# class Animal:
#     def __init__(self):
#         pass
#     def meow(self):
#         print("Meow Meow !")

# print(Animal.__name__)
# print(Animal.__base__)
# print(Animal.__dict__)

# thee_animal = Animal()
# thee_animal.meow()
# print(thee_animal.__dict__)


# ✅ Part 3: Create a Custom Metaclass
# Task 3:
# Write a metaclass that modifies the class at creation time.

# class UppercaseAttributes(type):
#     def __new__(cls,name, bases, dic):
#         new_dict = {}
        
#         for key,value in dic.items():
#             if  key.startswith("__") or key.endswith("__"):
#                 print(key)  # CHECK THE KEYS
#                 new_dict[key] = value
#             elif not key.startswith("_"):
#                 print(key)  # CHECK THE KEYS
#                 new_dict[key.upper()] = value

#         return super().__new__(cls,name,bases,new_dict)


# try:
#     class MyClass(metaclass = UppercaseAttributes):
#         name = "Lorem"
#         def __init__(self,name):
#             self.name = name
#     the_class = MyClass("Lorem")
#     print(MyClass.NAME)
# except Exception as e:
#     print(e)
    
    

# ✅ Part 4: Enforce Rules with Metaclass
# Task 4:
# Write a metaclass that enforces a rule: all class names must start with C.

# class MetaTwo(type):
#     def __new__(cls,name,bases,dic):
#         if not name.startswith("C"):
#             raise Exception("Class Name must be starts with C")
#         else:
#             print("Class created successfully")
#         return super().__new__(cls,name,bases,dic)


# try:

#     class ClassTwo(metaclass= MetaTwo) :
#         name = "Class"

# except Exception as e:
#     print(e)


# Task 5:
# Make a metaclass that adds a describe() method to every class that uses it.

# class MustHaveMethod(type):
#     def describe(cls):
#             print(f"This class is called {cls.__name__} and has attributes: {cls.__dict__.keys()}")
    
#     def __call__(cls, *args, **kwargs):
#         print("Creating instance...")
#         instance = super().__call__(*args, **kwargs)
#         instance.describe = cls.describe
#         return instance
    
#     def __new__(cls,name,bases,dic):
        
#         return super().__new__(cls,name,bases,dic)

# class X(metaclass=MustHaveMethod):
#     board_name = "XYZ"
#     def __init__(self,name,section):
#         self.name = name
#         self.section = section

# the_x = X("Tom","A")
# X.describe()
# the_x.describe()



# MetaClass Assignments – Level 2

# ✅ Assignment 1: Validate Required Method
# Goal: Ensure every class using the metaclass defines a method called run(). If not, raise an error.

# class MustHaveRunMethod(type):
#     def __new__(cls,name,bases,dic):
#         if "run" not in dic.keys():
#             raise Exception(f"{cls.__name__} must have run method")
#         return super().__new__(cls,name,bases,dic)

# try:
#     class Program(metaclass=MustHaveRunMethod):
#         def run(self):
#             print("Run Again")
    
#     the_prog = Program()
#     Program.run(the_prog)
#     the_prog.run()

#     class Race(metaclass=MustHaveRunMethod):
#         pass


# except Exception as e:
#     print(e)


# ✅ Assignment 2: Automatically Add Timestamp
# Goal: Add a class attribute created_at (with current timestamp) to every class created with this metaclass.

# Hint: Use datetime.datetime.now().

# class MetaTime(type):
#     created_at = datetime.datetime.now()
#     def __new__(cls,name,bases,dic):
#         dic["created_at"] = datetime.datetime.now()
#         return super().__new__(cls,name,bases,dic)


# class One(metaclass=MetaTime):
#     pass

# print(One.created_at)
# class Two(metaclass=MetaTime):
#     pass


# print(Two.created_at)


# ✅ Assignment 3: Count Class Creations
# Goal: Keep a global count of how many classes have been created with your metaclass.

# countOfClasses = 0

# class MetaCount(type):
#     def __new__(cls,name,bases,dic):
#         global countOfClasses
#         countOfClasses +=1
#         return super().__new__(cls,name,bases,dic)


# class Class_1(metaclass=MetaCount):
#     name = "Class One"


# class Class_2(metaclass=MetaCount):
#     name = "Class Two"


# print(countOfClasses)


# ✅ Assignment 4: Force Attribute Naming Convention
# Goal: Only allow attributes (defined inside class body) that are UPPERCASE. If any lowercase name is found, raise TypeError.

# class MetaUppercase(type):
#     def __new__(cls,name,bases,dic):
#         for key in dic.keys():
#             if not key.replace("-"or"_","").isupper() and not key.startswith("__") and not key.endswith("__"):
#                 raise Exception("Please only capital attributes are allowed like name -> NAME")
#         return super().__new__(cls,name,bases,dic)


# try:
#     class UpperOne(metaclass=MetaUppercase):
#         NAME = "lorem"
#         LAST_NAME = "IPSUM"
#     print(UpperOne.NAME)
#     print(UpperOne.LAST_NAME)
# except Exception as e:
#     print(e)


# ✅ Assignment 5: Restrict Inheritance
# Goal: Only allow classes that inherit from a specific base class like BaseModel.


# class BaseModelRequired(type):
#     def __new__(cls,name,bases,dic):
    
#         if BaseModel not in bases:
#                 raise Exception(f"{name} must be Inherit from (Base Model) class.")
#         return super().__new__(cls,name,bases,dic)

# class BaseModel:
#     def base(self):
#         print("Baby ko base pasand ha")


# try:
#     class User(BaseModel,metaclass=BaseModelRequired):
#         def __init__(self,name,roomNo):
#             super().__init__()
#             self.name = name
#             self.roomNo = roomNo
#     the_user = User("Tom",402)
#     the_user.base()

#     class Client(metaclass=BaseModelRequired):
#         pass
        
    
# except Exception as e:
#     print(e)



# 🧠 Metaclass Assignments – Level 3 & 4

# ✅ Assignment 6: Enforce Method Signature
# Goal: Ensure all methods in a class (defined using your metaclass) must have at least one parameter besides self (i.e., no method with only def method(self): is allowed).

# class EnforceArgs(type):
#     def __new__(cls,name,bases,dic):
#         for key,value in dic.items():
#             # print(key)
#             if inspect.isfunction(value):
#                 sig = inspect.signature(value)
#                 # print(sig)
#                 numPrams = sig.parameters
#                 # print(numPrams)
#                 if not (len(numPrams) > 1):
#                     raise Exception(f"Atleast 1 paramter is required in {name}.")
            
#         return super().__new__(cls,name,bases,dic)


# try:
#     class MyClass(metaclass=EnforceArgs):
#         def good(self,x,y):
#             print(x,y)
#     class MyClassTwo(metaclass=EnforceArgs):
#         def bad(self):
#             print("Bad")
    
# except Exception as e:
#     print(e)


# ✅ Assignment 7: Auto-Docstring Check
# Goal: Prevent class creation unless each method has a docstring.

# Hint: You can check using __doc__ on the function.


# class MustHaveDocs(type):
#     def __new__(cls,name,bases,dic):
#         for key,value in dic.items():
#             if inspect.isfunction(value):
#                 print(key)
#                 # print()
#                 doc_string = inspect.getdoc(value)
#                 # print(sign)
#                 if not doc_string:
#                     raise Exception(f"{key}() method of {name} class must have a docstring.")


#         return super().__new__(cls,name,bases,dic)


# try:
#     class Valid(metaclass=MustHaveDocs):
#         def hello(self):
#             """jngverjngjenrjgnerjnfjernjn"""
#             print("Hello")

#     class InValid(metaclass=MustHaveDocs):
#         def hello(self):
#             # """jngverjngjenrjgnerjnfjernjn"""
#             print("Hello")

# except Exception as e:
#     print(e)


# ✅ Assignment 8: Auto-Class Registry
# Goal: Automatically register every class created with the metaclass in a global registry for future lookup.
# register_class_list = {}

# class RegisterClass(type):
#     def __new__(cls,name,bases,dic):
#         register_class_list[name] = type(name,bases,dic)
#         return super().__new__(cls,name,bases,dic)


# class User(metaclass=RegisterClass):
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city

# class Client(metaclass=RegisterClass):
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city


# print(register_class_list)


# ✅ Assignment 9: Auto-Add __str__() Based on Attributes
# Goal: Dynamically add a __str__() method to every class that prints out all instance attributes like a JSON object


class AutoStr(type):
    def __new__(cls,name,bases,dic):
       
        def __str__(self):
           
            return json.dumps(self.__dict__)
        dic["__str__"] = __str__

        return super().__new__(cls,name,bases,dic)


class User(metaclass=AutoStr):
    def __init__(self,name,city):
        self.name = name
        self.city = city


print(User("Tom","Chicago"))


