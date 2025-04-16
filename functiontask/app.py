import math
# 📌 Basic Level

# 1️⃣ Write a function greet(name) that prints "Hello, [name]!" when called.
# def greet(name:str):
#     print(f"Hello, {name}!")

# greet('Sam')

# 2️⃣ Write a function square(n) that returns the square of n.
# def square(num:int):
#     return num**2
# print(square(2))

# 3️⃣ Write a function is_even(n) that returns True if n is even, otherwise False.
# def is_even(num:int):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(is_even(5))


# 📌 Intermediate Level

# 4️⃣ Write a function calculate_area(shape, value1, value2=0) that calculates the area of:

# Circle (π * r²) if shape is "circle"
# Rectangle (length * width) if shape is "rectangle"
# Triangle (0.5 * base * height) if shape is "triangle"

# def calculate_area(shape:str,value1:int,value2:int=0):
#     if shape == "circle":
#         return math.pi * (value1**2)
#     elif shape == "rectangle":
#         return value1*value2
#     elif shape == "triangle":
#         return 0.5*(value1*value2)
#     else:
#         return "Invalid Shape"

# print(calculate_area("circle", 7))        
# print(calculate_area("rectangle", 5, 10)) 
# print(calculate_area("triangle", 6, 4))

# 5️⃣ Write a function factorial(n) using recursion to find the factorial of n.
# def factorial(num):
#     if num<=1:
#         return 1
#     else:
#         print(factorial(num-1))
#         return num*factorial(num-1)

# print(factorial(5))

# 6️⃣ Write a function reverse_string(s) that returns the reversed string.
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Hello"))


# 📌 Advanced Level

# 7️⃣ Write a function count_vowels(s) that returns the number of vowels (a, e, i, o, u) in the given string.
# def count_vowels(s:str):
#     countVowel = 0
#     if s.count("a")>=1:
#         countVowel +=s.count("a")
#     if s.count("e")>=1:
#         countVowel +=s.count("e")
#     if s.count("i")>=1:
#         countVowel +=s.count("i")
#     if s.count("o")>=1:
#         countVowel +=s.count("o")
#     if s.count("u")>=1:
#         countVowel +=s.count("u")
#     return f"Vowels : {countVowel}"

# print(count_vowels("Hello World"))

# 8️⃣ Write a function fibonacci(n) that generates the first n Fibonacci numbers using recursion.
# fib = 0
# fibFind = 1
# def fibbonaci(n):
#    global fib,fibFind
#    if n>0:
#       print(fib)
#       fib,fibFind = fibFind,fibFind+fib
#       fibbonaci(n-1)

# fibbonaci(7)

# 9️⃣ Write a function find_max(*args) that takes multiple numbers and returns the maximum number.

# def find_max(*args, index=0, maxNum=None):
#     if maxNum is None:
#         maxNum = args[0]  

#     if index == len(args):  
#         return maxNum

#     if args[index] > maxNum:  
#         maxNum = args[index]

#     return find_max(*args, index=index+1, maxNum=maxNum)  

# print(find_max(10, 5, 30, 25, 100, 3))  


# 🔟 Write a function is_palindrome(s) that checks if a word is a palindrome (same forward and backward)

# def is_palindrome(s):
#     reverseStr = s[::-1]
#     if s == reverseStr:
#         return True
#     else:
#         return False

# print(is_palindrome("madad"))