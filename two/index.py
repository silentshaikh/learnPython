import random,string
# Task one
# print("Hello, World! Welcome to Python Programming. Let's start coding!")

# numOne = input("Enter a Number : ")
# numTwo = input("Enter a Number : ")
# optionList = ["Addition", "Subtraction","Multiplication","Division","Exponentiation"]
# if not numOne.replace(" ",'') or not numTwo.replace(" ",''):
#   print("Please Enter a Number")
# else:
#   if not numOne.isnumeric() or not numTwo.isnumeric():
#     print("Please Enter Only Number")
#   else:
#     numOne = int(numOne)
#     numTwo = int(numTwo)
#     print(" Choose one Option :")  
#     for index, option in enumerate(optionList, start=1):
#         print(f"{index}) {option}")
#     optionBox = input("Enter Your Option :")
#     if optionBox.lower() == "Addition".lower():
#       print(f"{optionBox.title()} = {numOne+numTwo}")
#     elif optionBox.lower() == "Subtraction".lower():
#       print(f"{optionBox.title()} = {numOne-numTwo}")  
#     elif optionBox.lower() == "Multiplication".lower():
#       print(f"{optionBox.title()} = {numOne*numTwo}")   
#     elif optionBox.lower() == "Division".lower():
#       print(f"{optionBox.title()} = {numOne/numTwo}")  
#     elif optionBox.lower() == "Exponentiation".lower():
#       print(f"{optionBox.title()} = {numOne**numTwo}")  
#     else:
#       print("Invalid Operation.")    
     

#password generator
# password = ''.join(random.choice(characters) for _ in range(length))
    # print(password)

def generatePassword(length:int):
    # get characters, numbers, special characters from module string
    passCharacters = string.ascii_letters
    passNumbers = string.digits
    passSpecial = string.punctuation
    characters = passCharacters+passNumbers+passSpecial
    # password generate
    ourPassword = ''
    for _ in range(length):
       # add random character , digit , special characters on each iteration
       ourPassword += random.choice(characters)  
    print(f"Generated Password = {ourPassword}")
    
# if here any error like type in input or function , so it will handle the error with a user friendly message
try:
    # input for ask the length of password
  passLength = int(input("Enter a number :"))
  #check length is greater than zero 
  if(passLength>0):
     generatePassword(passLength)
  else:
     print("Please enter number that's greater than zero !")   
except:
  print("Plz enter only a number (0-9)")