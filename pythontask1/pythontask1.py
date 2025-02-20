# Question 01

# Write a Python program that takes an integer as input.

# If the number is positive, print "Positive number"
# If the number is negative, print "Negative number"
# If the number is zero, print "Zero"

# Bonus: Also check if the number is even or odd.


numInput = int(input("Enter a Number"))
evenOrOdd = "Even" if numInput %2 ==0 else "Odd"
if numInput > 0:
    print('Positive number')
    print(evenOrOdd)
elif numInput < 0:
    print('Negative Number')
    print(evenOrOdd)
else:
    print('Zero')   
    print(evenOrOdd)     




# Question 02

# Write a Python program that takes two numbers as input and prints their:

# Sum
# Difference
# Product
# Quotient (division)
# Modulus
# Exponentiation (power)

# Bonus: Try using floor division (//).

numOne = int(input('Enter a Number'))
numTwo = int(input('Enter a Number'))

if numOne and numTwo :
    print('Sum : ', numOne+numTwo)
    print('Difference : ',numOne-numTwo)
    print('Product : ',numOne*numTwo)
    print('Quotient : ', numOne/numTwo)
    print('Modulus : ',numOne%numTwo)
    print('Exponentiation : ',numOne**numTwo)
    print('Floor Division : ', numOne // numTwo) # like Math.floor()
else:
    print('Please Enter a Number of greater than or less than equal to')




# Question 03

# Write a Python program where:

# You declare a variable x = 10.
# Use assignment operators (+=, -=, *=, /=, %=, //=, **=) to modify x step by step.
# Print the value of x after each operation.

#  Bonus: Try using &=, |=, ^= operators with another number.

x = 10
x+=5
print('Sum',x)
x-=5
print('Division',x)
x*=5
print('Product',x)
x/=5
print('Quotient',x)
x%=5
print('Modulus',x)
x**=5
print('Exponentiation',x)




# Question 04

# Write a program that takes two numbers as input and:

# Checks if the first number is greater than, less than, equal to, or not equal to the second number.
# Prints True or False for each comparison.
# Bonus: Include >= and <= checks.


numOne = int(input('Enter a Number'))
numTwo = int(input('Enter a Number'))

print(numOne>numTwo)
print(numOne<numTwo)
print(numOne==numTwo)
print(numOne!=numTwo)
print(numOne>=numTwo)
print(numOne<=numTwo)



# Question 05

# Write a Python program that:

# Takes three boolean inputs (True or False).
# Uses AND (and), OR (or), and NOT (not) operators to check different conditions.
# Prints the results.


boolOne = bool(input('Enter a Boolean'))
boolTwo = bool(input('Enter a Boolean'))
boolThree = bool(input('Enter a Boolean'))
print(boolOne or boolTwo)
print(boolTwo and boolThree)
print(not boolThree and boolOne)
print(not boolOne or boolThree and boolTwo)


# Question 06

# Write a program that:

# Takes an integer input from the user and converts it into a float and a string.
# Takes a float input and converts it into an integer and a string.
# Takes a string input (number as text) and converts it into an integer and float.

#  Bonus: What happens if you try converting "Hello" into an integer? Try it and handle the error.


try:
    intInput = int(input('Enter a Integer : '))
    print('Float : ', float(intInput))
    print('String : ',str(intInput))
except ValueError:
    print('Error Can not convert string to number')

floatInput = float(input('Enter a Float : '))
print('Integer : ', int(intInput))
print('String : ',str(intInput))

stringInput = input('Enter a String as Number : ')
print('Integer : ', int(intInput))
print('float : ',float(intInput))


# Question 07

# Write a Python program that:

# Declares five different types of variables (integer, float, string, boolean, list).
# Prints their values and data types using type().
# Bonus: Change one variable type dynamically and print its new type.


strValue = "Hello World"
intValue = 420
floatValue = 44.3
boolValue = True
listValue = [1,2,3,4,5]
print(type(strValue))
print(type(intValue))
print(type(floatValue))
print(type(boolValue))
print(type(listValue))
dynamicType = intValue+floatValue
print(type(dynamicType))


# Question 08

# Write a Python program that:

# Takes a number as input and prints "Even" if it's even, otherwise "Odd", using a single-line if-else (ternary operator).


numInput = int(input('Enter a Number : '))
print('Even') if numInput %2 == 0  else print('Odd')


# Question #09

# Write a Python program that:

# Takes a user's age and prints:
# "Child" if age < 12
# "Teenager" if age is between 13 and 19
# "Adult" if age is 20 or above

#  Bonus: Solve this in one line using chained if-elif-else.



userAge = int(input("Enter You Age"))
if userAge <=12:
    print('Child')
elif userAge  >=13 and userAge <=19:
    print('Teenager')     
elif userAge >=20:
    print('Adult')

print('Child') if userAge <=12 else print('Teenager') if userAge  >=13 and userAge <=19 else print("Adult")

