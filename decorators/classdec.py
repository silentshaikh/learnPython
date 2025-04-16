#  Task 1: Track Instance Creation
# Create a class decorator @track_creation that:

# Prints a message every time an instance of the class is created.
# Keeps a count of how many instances were created.
# Adds a method get_instance_count() to the class to return the count.

def track_creation(cls):
    cls._instance_count = 0
    original_init = cls.__init__
    def new_init(self,*args,**kwargs):
        cls._instance_count += 1
        print(f"{cls.__name__} instance {cls._instance_count} created") 
        original_init(self,*args,**kwargs)
    def get_instance_count(self):
            return f"Total {cls.__name__} instances {cls._instance_count}"

    
    cls.__init__ = new_init
    cls.get_instance_count = get_instance_count
    return cls





@track_creation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author



book = Book("Dumpty","lorem")
book2 = Book("Dumty","lorem")
print(book2.get_instance_count())



# ✅ Task 2: Add Timestamp to Object Creation
# Create a decorator @add_created_time that:

# Adds a created_at attribute to every object of a class.
# The created_at value should be the current timestamp (datetime.now())
# Use it on a class called Order.
from datetime import datetime

def add_created_time(cls):
     cls.created_at = None
     original_init = cls.__init__
     def new_init(self,*arg,**kwargs):
          cls.created_at = datetime.now()
          original_init(self,*arg,**kwargs)
     cls.__init__ = new_init
     return cls

@add_created_time
class Order:
    def __init__(self, order_id):
        self.order_id = order_id

o1 = Order(123)
print(o1.created_at)  # Should print a timestamp


#  Bonus Task (Optional): Combine Decorators

# Apply both @track_creation and @add_created_time to a new class Invoice.
# Make sure both decorators work correctly when applied together.

@track_creation
@add_created_time
class Invoice():
     def __init__(self,order_id,title,author):
          self.order_id = order_id
          self.title = title
          self.author = author

inVoice = Invoice(1234,"Dumpty","Lorem")
print(inVoice.get_instance_count())
print(inVoice.created_at)
          