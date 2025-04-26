import re
# Q1. Basic Exception Handling
# Write a Python program that:

# Takes two numbers from the user (input).

# Divides the first number by the second.

# Handle exceptions for:

# ZeroDivisionError (if the second number is zero)

# ValueError (if user inputs non-numeric values)

# try:
#     num_1 = int(input("Enter a Number : "))
#     num_2 = int(input("Enter a Number : "))
#     print(f"{num_1} / {num_2} : {num_1/num_2}")

# except ZeroDivisionError:
#     print("Don't Enter Zero in the Second Input")
# except ValueError:
#     print("Plz enter only a number")

#-------------------------------------------------------------------------------

# Q2. Multiple Exceptions
# Write a program that:

# Takes a list and an index number as input.

# Prints the element at that index.

# Handle:

# IndexError (invalid index)

# TypeError (if list or index input is wrong)

# try:
#     num_list = [1,2,3,4,5,6,7,8,9,10]
#     indexInp = input("Enter an Index : ")
#     print(num_list[indexInp])
# except IndexError:
#     print("Please Enter a Valid Index")
# except TypeError:
#     print("List must be list and Index must be integer (0-9)")
# except ValueError:
#     print("Plz enter only a number (0-9)")

# ------------------------------------------------------------------------------

# Q3. Else and Finally Block
# Write a program that:

# Asks the user for a filename.

# Tries to open and read the file.

# If successful, print the contents.

# If the file does not exist, show a friendly error.

# In finally block, print "Program finished reading file."


# try:
#     fileName = input("Enter the name of the file : ")
#     with open(fileName,"r") as readFile:
#        the_read =  readFile.read()
# except FileNotFoundError:
#     print("File is not exist here")
# else:
#        print(the_read)
# finally:
#      print("Program finished reading file.")

# ---------------------------------------------------------------------------


# Q4. Custom Exception
# Create a custom exception called AgeTooSmallError.
# Write a program that:

# Takes the user's age as input.

# If age < 18, raise AgeTooSmallError with the message "Age must be 18 or above."

# Otherwise, print "Access granted."

# class AgeTooSmallException(Exception):
#     def __init__(self,message,error_code):
#         super().__init__(message)
#         self.message = message
#         self.error_code = error_code
    
#     def __str__(self):
#         return f"{self.message} (Error Code: {self.error_code})"


# def check_age(age):
#    if age >= 18:
#         print("Access granted")
#    else: 
#         raise AgeTooSmallException("Age must be 18 or above.",420)


# try:
#     the_age = int(input("Enter Your Age : "))
#     check_age(the_age)
# except AgeTooSmallException as age_error:
#     print(age_error)

# --------------------------------------------------------------------------------


# Q5. Exception inside a Function
# Create a function called calculate_square_root(x):

# It should return the square root of x.

# If x is negative, raise a ValueError saying "Cannot calculate square root of a negative number."

# def calculate_square_root():

#     squareInp = int(input("Enter a Number : "))
#     if squareInp>0:
#         print(f"Square of {squareInp} : {squareInp**2}")
#     else:
#         raise ValueError("Please Enter only Positive Number")

# calculate_square_root()

# ------------------------------------------------------

# Q6. Nested Try-Except
# Write a program that:

# Takes two numbers from the user.

# First tries to convert them to integers inside a try block.

# Then tries to divide them inside another nested try block.

# Handle all errors properly and show friendly messages.

# numOne = input("Enter a Number : ")
# numTwo = input("Enter a Number : ")
# try:
#     numOne = int(numOne)
#     numTwo = int(numTwo)
#     try:
#         print(f"{numOne} / {numTwo} : {numOne/numTwo}")
#     except ZeroDivisionError:
#         print("Plz second number must be non-zero")
# except ValueError:
#     print("Plz Enter Only Number")

# -----------------------------------------------------------------

# Q7. Catching All Exceptions
# Write a program that:

# Asks the user for two integers.

# Divides the first by the second.

# If any unexpected error happens, catch it using a generic except Exception as e and print the error message.

# try:
#     num_one = int(input("Enter a Number : "))
#     num_two = int(input("Enter a Number : "))

#     print(f"{num_one} / {num_two} : {num_one/num_two}")

# except Exception as e:
#     print("Exception Error : ", e)

# --------------------------------------------------------------------------------------------------------------

# Q8. Try-Except inside a Loop
# Write a program that:

# Repeatedly asks the user to enter a number.

# If the user enters something invalid (not a number), catch the error and ask again.

# Exit the loop when the user types "exit".

# After exiting, print all the numbers entered by the user as a list.

# num_list = []
# while True:
#     try:
#         num_inp = input("Enter a Number : ")
#         if num_inp.isdigit():
#            num_inp = int(num_inp) 
#            num_list.append(num_inp)
#         elif num_inp == "exit":
#             break
#         else:
#             raise ValueError("Please Enter Only a Number")
            
#     except Exception as the_error:
#         print(the_error)


# print(num_list)
        
# -------------------------------------------------------------------------------------------------------   

# Q9. Create and Handle Multiple Custom Exceptions
# Create two custom exceptions:

# NegativeDepositError

# WithdrawLimitError

# Write a BankAccount class with methods:

# deposit(amount) ➔ Raise NegativeDepositError if amount is negative.

# withdraw(amount) ➔ Raise WithdrawLimitError if amount > balance.

# Demonstrate usage by creating an object and performing deposits and withdrawals.

# class NegativeDepositError(Exception):
#     def __init__(self,message):
#         super().__init__(message)
#         self.message = message
    
#     def __str__(self):
#         return f"{self.message} ."
    

# class WithdrawLimitError(Exception):
#     def __init__(self,message):
#         super().__init__(message)
#         self.message = message
    
#     def __str__(self):
#         return f"{self.message} ."


# class BankAccount:
#     def __init__(self,current_amount):
#         self.current_amount = current_amount
    
#     def deposit(self,amount):
#         if amount>=0:
#             self.current_amount += amount
#             print(f"The Current Amount after deposit is : {the_bank_account.current_amount} $ .")
#         else:
#             raise NegativeDepositError("Dear Customer, Your Deposit Amount must be greater than zero") 
    
#     def withdraw(self,amount):
#         if amount > self.current_amount:
#             raise WithdrawLimitError(f"Dear Customer, You can't withdraw {amount} because your current amount is {self.current_amount}")
#         else:
#             if amount<0:
#                raise NegativeDepositError("Dear Customer , Your withdraw amount must be greater than zero.")
#             else:
#                 self.current_amount -= amount
#                 print(f"The Current Amount after withdraw is : {the_bank_account.current_amount} $ .")


# try:
#     the_bank_account = BankAccount(500000000000000000000000000)
#     the_bank_account.deposit(800)
    
#     the_bank_account.withdraw(-800)
# except Exception as e:
#     print(e)

# ----------------------------------------------------------------------------------------------

# Q10. Resource Management with Exception Handling
# Write a program that:

# Opens a file and reads its contents.

# Ensure the file is properly closed, even if an exception happens, using a try-finally block (without using with statement).

# try:
#     open_file = open("text.txt","r")
#     read_the_file = open_file.read()
#     print(f"\n{read_the_file} \n ")
# except Exception as e:
#     print(e)
# finally:
#     open_file.close()
#     print(open_file.closed)

# ----------------------------------------------------------------------------------------------------------

# Q11. Raising Exceptions in Loops
# Write a program that:

# Continuously asks the user to enter a password.

# Password Rules:

# Length must be at least 8 characters.

# Must contain at least one number.

# Raise ValueError with appropriate messages if the password doesn't meet rules.

# Keep asking until a valid password is entered


# while True:
#     try:

#         passwordInp = input("Enter a Password : ")
#         if len(passwordInp) >=8:
#             if re.match(r"^[a-zA-Z0-9_\.\%\+\-\@\#\$\^]+$",passwordInp):
#                 # break
#                 if re.search(r"[a-zA-Z]", passwordInp) and re.search(r"[0-9]", passwordInp):
#                     print(f"\n Password : {passwordInp} \n")
#                     break
#                 else:
#                     raise ValueError("Please enter atleast one number")
#             else:
#                 raise ValueError("Please enter atleast one number")
#         else:
#             raise ValueError("Password Must be 8 character and atleast one number and one symbol")
#     except Exception as e:
#         print(e)
#         continue

#  -----------------------------------------------------------------------------------------------------------


# Q12. Handling Exceptions in List Comprehensions
# Write a program that:

# Given a list of mixed data types (integers, strings, floats),

# Use list comprehension to create a new list that only contains integers.

# Handle errors gracefully if typecasting fails.


# try:
#     data = [1, 'hello', 3.5, 2, '42', 'world', 7,True,False,["lorem"],None]
#     num_list = [int(num) for num in data if isinstance(num,int)]
#     print(f"Num List : {num_list}")

# except Exception as e:
#     print(e)


# ---------------------------------------------------------------------------------------------------
    