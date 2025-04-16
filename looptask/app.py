# Basic Level

# Print Numbers: Write a program that prints numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)

# num1 = 1

# while num1<=10:
#     print(num1)
#     num1+=1


# Even Numbers: Print all even numbers from 1 to 20 using a while loop.
# for i in range(1,21):
#     if (i % 2) == 0:
#         print("Even Number : ",i)
# num2 = 1
# while num2<=20:
#     if (num2 % 2) == 0:
#         print("Even Number : ",num2)
#     num2+=1


# Sum of Numbers: Write a program that calculates the sum of numbers from 1 to 50 using a for loop.
# sums = 0
# for i in range(1,51):
#     sums += i
# print(sums)
# num3 = 1
# sums2 = 0
# while num3<=50:
#     sums2 += num3
#     num3+=1
# print(sums2)


# Multiplication Table: Take a number input from the user and print its multiplication table up to 10 using a loop.
# numInput = int(input("Enter a Number : "))
# for i in range(1,11):
#     print(f'{numInput} * {i} = {i*numInput}')

# num4 = 1
# while num4<=10:
#     print(f'{numInput} * {num4} = {num4*numInput}')
#     num4+=1


# Reverse Order: Print numbers from 10 to 1 using a while loop.
# for i in range(10,0,-1):
#     print(i)
# num5 = 10
# while num5>=1:
#     print(num5)
#     num5-=1


# Intermediate Level
# Factorial Calculation: Write a program to find the factorial of a number using a loop.
# fact = 5
# for i in range(5,0,-1):
#     if(i<=1):
#         fact = fact*1
#     else:
#         fact = fact*(i-1)
# print(fact)
# num6 = 5
# while num6>=1:
#     if(num6<=1):
#         fact*=1
#     else:
#         fact *= num6-1
#     num6 -=1
# print(fact)


# Count Digits: Take a number as input and count how many digits it has using a loop.
# inpCount = int(input("Enter a number : "))
# numCount = 0
# for num in str(inpCount):
#     numCount +=1
# while numCount < len(str(inpCount)):
#     numCount+=1

# print(f"The Total Count of {inpCount} is {numCount}")


# Find Maximum in a List: Given a list of numbers, find the largest number using a loop.
# numList = [10,20,30,40,50,60,200,70,80,90,100]
# highNum = 0
# for num in numList:
#     if num > highNum:
#         highNum = num

# print(f"Highest Number is {highNum}")


# Fibonacci Series: Print the first 10 numbers of the Fibonacci series using a loop.
# fib = 1
# num = 1
# for i in range(1,11):
#    if fib<=10:
#        print(fib)
#        fib,num = num,fib+num 
# num7 = 1
# while num7<=10:
#     if fib<=10:
#         print(fib)
#         fib,num = num,fib+num
#     num7+=1


# Advanced Level


# Prime Number Check: Write a program that checks if a given number is prime or not using a loop.
# primeInput = int(input("ENter a Number : "))
# isPrime = True
# for num in range(2,primeInput):
#     if (primeInput % num) == 0:
#         isPrime = False
#         break

# if isPrime:
#     print(f"{primeInput} is a Prime Number.")
# else:
#     print(f"{primeInput} is not a Prime Number.")


# Pattern Printing: Print the following pattern using loops:
# *
# **
# ***
# ****
# *****
# stars = ""
# for i in range(1,6):
#     stars = "*" *i
#     print(stars)


# Palindrome Check: Write a program to check if a word is a palindrome using a loop.
# word = "theft"
# reverseWord = ""
# for i in word[::-1]:
#     reverseWord += i

# if word == reverseWord:
#     print(f"{word} is a Palindrome")
# else:
#     print(f"{word} is not a Palindrome")


# FizzBuzz: Print numbers from 1 to 50, but:
# Print "Fizz" for multiples of 3
# Print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of both 3 and 5
# for num in range(1,51):
#     if (num%5) == 0 and (num%3) == 0:
#         print(f"{num} is FizzBuzz")
#     elif (num%3) == 0:
#         print(f"{num} is Fizz")
#     elif (num%5) == 0:
#         print(f"{num} is Buzz")
    
#     else:
#         print(num)


# Number Pyramid: Print the following number pyramid using loops:
#    1
#   121
#  12321
# 1234321
row =4  # Change this to increase the pyramid height
for i in range(1,5):
    leftSide = "".join(str(num) for num in range(1,i+1)) # generate (1,12,123,..) 
    rightSide = leftSide[-2::-1] # Reverses left_side excluding the last character
    # print(rightSide)
    print(" " * (row-i) + (leftSide+rightSide))

