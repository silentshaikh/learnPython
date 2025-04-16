# Create a class Temperature with:

# A private attribute __celsius.
# A @property called fahrenheit to convert Celsius to Fahrenheit.
# A @fahrenheit.setter to set Fahrenheit and update Celsius internally.

# class Temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     @property
#     def fahrenheit(self):
#         return (self.celsius * 9/5) +32
#     @fahrenheit.setter
#     def fahrenheit(self,value):
#         self.celsius = (value - 32) * 5/9

# temp = Temperature(0)
# print(temp.fahrenheit)
# temp.fahrenheit = 100
# print(temp.celsius)


#  Person Age Control
# Create a class Person:

# Private attribute __age.
# A @property for age with a setter.
# Raise an error if age is less than 0 or greater than 120.
# class Person:
#     def __init__(self,age):
#         self.__age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value<0 or value>120:
#             raise "Enter a age (0-120)"
#         else:
#             self.__age = value

# person = Person(25)
# person.age = 26
# print(person.age)
# person.age = -2 


# 🧪 Intermediate Level
# 3. Bank Account with Balance Validation
# Class BankAccount:

# Protected attribute _balance.
# @property balance that returns _balance.
# @balance.setter that prevents setting a negative balance.
# Add method deposit and withdraw using balance property.
# class BankAccount:
#     def __init__(self,balance):
#         self._balance = balance
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self,value):
#         if value<0:
#             raise "Invalid Balance"
#         else:
#             self._balance = value
#     def deposit(self,value):
#         if value<0:
#             raise "Invalid Amount for deposit"
#         else:
#             self._balance += value
#     def withdraw(self,value):
#         if value<0:
#             raise "INvalid Amount for withdraw"
#         elif value>self._balance:
#             raise Exception(f"Cash in your Account is only {self._balance} so you can't withdraw {value}")
#         else:
#             self._balance -=value

# backAccount = BankAccount(100)
# print(backAccount.balance)
# backAccount.balance = 300
# print(backAccount.balance)
# backAccount.deposit(45)
# print(backAccount.balance)
# backAccount.withdraw(400)
# print(backAccount.balance)


# 4. Product Discount Calculator
# Class Product:

# Private __price and __discount.
# @property final_price that applies the discount dynamically.
# @discount.setter that doesn’t allow more than 50%.
# class Product:
#     def __init__(self,price,discount):
#         self.__price = price
#         self.__discount = discount
#     @property
#     def discount(self):
#         return self.__discount
#     @discount.setter
#     def discount(self,value):
#         if value>0.5 or value < 0 :
#             raise Exception(f"You can only get 50% or less discount")
#         else:
#             self.__discount = value
#     @property
#     def final_price(self):
#         if self.__discount>0.5:
#             raise Exception(f"You can only get 50% or less discount")
#         return self.__price * (1-self.__discount)

# product = Product(100,0.5)
# print(product.final_price)
# product.discount = 0.5
# print(product.final_price)
# print(product.discount)


# 🧪 Bonus: Advanced Practice (Optional)
# 5. Smart Rectangle
# Class Rectangle:

# Private __width and __height.

# Properties:
# area: returns width * height.
# perimeter: returns 2*(width + height).
# is_square: returns True if width == height.
class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    @property
    def area(self):
        return self.__width*self.__height
    @property
    def perimeter(self):
        return 2*(self.__width + self.__height)
    @property
    def issquare(self):
        if self.__height == self.__width:
            return True
        else:
            return False

rect = Rectangle(10,10)
print(rect.area)
print(rect.perimeter)
print(rect.issquare)