import math,sys
# # Question #01
# # . Basic Number Types
# # Create three variables:
# # An integer (int) variable with a value of 100.
# # A floating-point (float) variable with a value of 25.75.
# # A complex number (complex) variable with a value of 3 + 4j.
# # Print the type of each variable using the type() function.

# intVal = 100
# floatVal = 25.75
# complexVal = 3+4j
# print("int : ",intVal)
# print("float : ",floatVal)
# print("complex : ",complexVal)


# # Question #02
# # Perform the following calculations and print the results:

# # Sum of 150 and 27.5
# # Difference between 500 and 123
# # Product of 12 and 3.5
# # Quotient of 144 divided by 12
# # Floor division of 17 by 4
# # Remainder when 29 is divided by 5
# # 2 raised to the power of 5

# print("Sum : ",150+27.5)
# print("Subtract : ",500-123)
# print("Multiply : ",12*3.5)
# print("Divide :",144/12)
# print("Floor Division : ", 17//4)
# print("Remainder : ",29%5)
# print("Exponentiation : ", 2**5)


# # Question #03
# # Type Conversion
# # Convert an int value (250) into float and complex types.
# # Convert a float value (99.99) into an int.
# # Convert a string ("1234") into an int.

# convInt = int(99.99)
# convFloat = float(250)
# strToInt = int("12345")
# print("float to int",convInt)
# print("int to float",convFloat)
# print("string to int",strToInt)


#Question #04

#  Mathematical Operations with User Input
# numOne = float(input("Enter a Number : "))
# numTwo = float(input("Enter a Number : "))

# print("Absolute Difference : ",abs(numOne-numTwo))
# print(f"Maximum : {numOne if numOne>numTwo else numTwo} and Minimum : {numOne if numOne<numTwo else numTwo}")
# print(f"Square Root : {numOne} = {math.sqrt(numOne)} & {numTwo} = {math.sqrt(numTwo)}")
# print(f"Two Decimal Point : {round(numOne,2)} , {round(numTwo,2)}")
# numOne = int(numOne)
# numTwo = int(numTwo)
# print(f"Binary : {bin(numOne)} , {bin(numTwo)}")
# print(f"Octal : {oct(numOne)} , {oct(numTwo)}")
# print(f"Hexadecimal : {hex(numOne)} , {hex(numTwo)}")


# Question 05
# Factorial Calculator
# Write a function factorial(n) that takes an integer n as input and returns its factorial.
# Implement this using a for loop.
# Ensure the function handles edge cases (e.g., 0! = 1).

# def factorial(n):
#     for num in range(n,0,-1):
#         n *= (num-1) if num>1 else 1
#     print(n)
# factorial(5)


# Question 06
# Fibonacci Series Generator
# Write a function that generates the first n numbers in the Fibonacci sequence.
# The function should accept a user input n and return a list of Fibonacci numbers.

# def fibonaci(n):
#     a ,b = 0,1
#     # print(a,b)
#     for i in range(n):
#         yield a
#         a,b = b,a+b

# print(list(fibonaci(5)))


#Question 07
# Armstrong Number Checker
# A number is an Armstrong number if the sum of its digits raised to the power of the number of digits is equal to the number itself.
# Example: 153 = (1^3) + (5^3) + (3^3) = 153
# Write a function is_armstrong(num) to check if a given number is an Armstrong number.

# to check whether the given number is armstrong or not
# without using power function

# num = 153
# s = num
# b = len(str(num))

# sum1 = 0
# while num != 0:
#     r = num%10
#     sum1 = sum1 + (r**b)
#     num = num//10
# print(sum1)
# if s == sum1:
#     print("The Number is Armstrong :",s)
# else:
#      print("The Number is not an Armstrong :",s)
# print(1//10)


#Question 08

# Prime Number Checker
# Write a function is_prime(n) that checks if a number is prime.
# Optimize it to check divisibility up to sqrt(n) for better efficiency.
# Test the function with different values.

# isPrime = False
# def primNumber(n):
#     global isPrime
#     for x in range(2,n):
#         if n % x == 0:
#             isPrime = True
#             break


# primNumber(10)
# if isPrime:
#     print("iIt's not a prime number")
# else:
#     print("It's a Prime Number")

# Question 09
# Reverse an Integer
# Write a function reverse_integer(n) that takes an integer and returns its reversed version.

# def reverseInteger(num):
#     numToStr = str(num).replace(" ","")
#     if numToStr.startswith("-"):
#         strToList = list(numToStr)
#         strToList.remove("-")
#         listToStr =f"-{"".join(strToList[::-1])}"
#         strToNum = int(listToStr)
#         return strToNum
#     else:
#         strReverse = numToStr[::-1]
#         strToNum = int(strReverse)
#         return strToNum
    
# print(reverseInteger(-12345))

# Question 10
# Number Pattern Printing

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j)

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j)

#Question 11
# Find the Largest Palindromic Number in a Range
# Write a function that finds the largest palindromic number within a given range [a, b].
# A palindromic number reads the same forward and backward (e.g., 121, 1331, 4884).

# def largestPalindrome(num1,num2):
#     global larg
#     larg = 0
#     for n in range(num1,num2+1):
#         reverseNum = str(n)[::-1]
#         if int(reverseNum) == n :
#             larg = int(reverseNum)
#             if int(reverseNum) > larg:
#                 larg = int(reverseNum)
#     print(larg)

# largestPalindrome(10,100)

# Question 12
# Function to find GCD using the Euclidean algorithm

# def findGcd(a,b):
#     while b:
#         a,b = b,a%b
#     return a

# # Function to find LCM using GCD
# def findLcm(a,b):
#     # return (a*b) // math.gcd(a,b)
#     return (a*b) // findGcd(a,b)

# numOne = 12
# numTwo = 18
# ourGcd = findGcd(numOne,numTwo)
# ourLcm = findLcm(numOne,numTwo)

# print(f"GCD of {numOne} and {numTwo} is {ourGcd}.")
# print(f"LCM of {numOne} and {numTwo} is {ourLcm}.")

#Question 13
# Collatz Conjecture (Hailstone Sequence)
# The Collatz sequence is defined as follows:
# Start with any positive integer n.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Repeat this process until n becomes 1


# def collatzSequence(num):
#     while num !=1:
#         if num %2 == 0:
#             num = num //2
#             print(num)
#         else:
#             num  = (num * 3)+1    
#             print(num)

# collatzSequence(6)

# x = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# print(x)
# print(sys.getsizeof(x))

# print(56.78748957389486278631892647826745162365126427863589379748976376525346142453145234264523765734685)
# print(round(0.1 + 0.2, 2))  # 0.3

from decimal import Decimal, getcontext

getcontext().prec = 50  # Set precision to 50 decimal places

d1 = Decimal(1) / Decimal(7)
print(d1)  

  
 
    


