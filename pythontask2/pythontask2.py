import math,random
# Question 01
# Create a program that takes a year as input and determines if it's a leap year.
# Rules:

# A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.
# 🔹 Bonus: Extend the program to check if a date (DD-MM-YYYY) is valid.

# take an input to write an leap year
leapYear = int(input('Enter a Year'))
#check if a year is a leap year or not
if(leapYear %4==0 or leapYear %400==0):
    print('Leap Year')
else:
    print('Not a Lear Year')    



# Question 02
# Create a Simple Calculator where a user enters two numbers and an operator (+, -, *, /, %, **, //).

# The program should perform the operation and display the result.
# Handle division by zero error
# 🔹 Bonus: Use the math module to calculate square root, logarithm, and trigonometric functions.

# give an input to select the action for user
calcOptions = input('Enter You Options : ')
# give an input to calculate the numbers
numOne =  float(input("Enter a Number : "))
#check if option is equal to "sqroot" or not
if calcOptions.lower() == "sqroot".lower():
     print('Square Root: ', math.sqrt(numOne)) 
else :
    # if option is not equal to "sqroot" so the second input of number is here 
        numTwo = float(input("Enter a Number : "))
        if calcOptions.lower() == "sum".lower():
         print('Sum : ',numOne+numTwo)
        elif calcOptions.lower() == "minus".lower():
            print('Difference: ',numOne-numTwo)
        elif calcOptions.lower() == "multiply".lower():
            print('Product: ',numOne*numTwo)
        elif calcOptions.lower() == "division".lower():
            print('Quotient: ',numOne/numTwo)
        elif calcOptions.lower() == "exponent".lower():
            print('Exponentiation: ',numOne**numTwo)      
        elif calcOptions.lower() == "modulus".lower():
            print('Remainder: ',numOne%numTwo)                      
        else:
         print('INvalid Option')                



# Question 03

# Create a number guessing game where:

# The program generates a random number between 1 and 100.
# The user has to guess the number.
# The program gives hints like:
# "Too High!" if the guess is greater than the number.
# "Too Low!" if the guess is smaller than the number.
# "Correct! You Win!" if the guess is right.
# 🔹 Bonus: Limit the number of attempts to 5 and print "Game Over!" if the user fails.

#Chances to play the game
gameCount = 10
randNum  = math.floor(random.random()*100+1) # generate random number from 1 to 100

# if count will zero so the game will end
while(gameCount>0):
    # take an input where can guess the number
    userNum = int(input("Guess a Number : "))
    if(userNum == randNum):
        print('You Won !')
        break
    elif(userNum > randNum) :
        print('Your Number is Too High !')    
    elif(userNum<randNum):
        print('Your Number is Too Low !')  
    elif userNum != randNum:
        print('You Lost the Game')    
        break
    #decrement by 1 when user doesn't guess the number 
    gameCount -=1
    # show the chances that user have
    print(gameCount.__str__()+' Chances you have !')      



# Question 04
# Create a game score system where:

# A player's score starts at 0.
# The player gains points based on certain actions:
# += 10 for small achievements
# += 20 for medium achievements
# += 50 for big achievements
# The score can be reduced by mistakes:
# -= 5 for small mistakes
# -= 15 for big mistakes
# Bonus: Add a multiplier system where a player can get double points under special conditions.

playerScore = 0 # score of player
gameOn = True
while(gameOn):
    # input for write the action of user
    gameAction = input("Enter an Action:")
    # give points according to action
    if gameAction.lower() == "small achievements".lower():
        playerScore +=10
    elif gameAction.lower() == "medium achievements".lower():
        playerScore +=20
    elif gameAction.lower() == "big achievements".lower():    
        playerScore +=50
    elif gameAction.lower() == "small mistakes".lower():    
        # check if score is less or greater than equal to 5
         if(playerScore>=5):
                playerScore -=5
         else:
             playerScore = 0 

    elif gameAction.lower() == "big mistakes".lower():    
        # check if score is less or greater than equal to 15
        if(playerScore>=15):
            playerScore -=15
        else:
            playerScore = 0
    else:
        print('### Game has Ended ###')
        # Score of the Player after the match
        print("Player Score : ", playerScore)        
        break
    print('Current Score :',playerScore)


# Question 05


# Create a login system where:

# The user enters a username and password.
# The system checks if they are correct.
# If the user enters the wrong password three times, lock the account for security reasons
# 🔹 Bonus: Add a captcha check (a random math question) before the final attempt.

# username and password that user enter on the input
username = "abdulmoiz"
password = "1234567"
wrongCount = 0 # if username and password is wrong so it will increment by 1
login= True
while(login):
    userInput = input('Entr Your Name : ')
    passInput = input("ENter Your Password : ")
    # check username and is correct or not
    if(userInput.lower() == username.lower() and passInput.lower() == password.lower()):
        print('Dear '+username+', You have logged-in successfully')
    else:
        if(userInput.lower() != username.lower()):
            print('Username is Incorrect')    
        else:
            print('Password is Incorrect')

            #increment by 1 when username or password is incorrect  
        wrongCount +=1

        #Account will lock for several reason 
        if(wrongCount >=3):
            print('Your Account has locked for security reasons')      
            login = False


# Question 06
# Create a bank deposit calculator where:

# The user enters an initial deposit (float).
# The user enters a number of years (integer).
# The system calculates the total amount with an annual interest rate of 5%.
# 🔹 Bonus: Format the output to two decimal places and display results with currency symbols ($).

# user initial deposit
initialDeposit = float(input('Enter Your Initial Deposit : '))
numOfYears = int(input('Enter a Year : '))

#interest rate
interest_rate = 0.05  #5%

# calculate the final amount using compound interest formula = A = P(1+r)^t
finalAmount = initialDeposit*(1+interest_rate)**numOfYears

#Display the result woth two decimalplaces and currency format
print(f"Total Amount after {numOfYears} years: ${finalAmount:.2f}")


#Question 07
# Create a shopping cart where:

# A dictionary holds products:
# python
# Copy
# Edit
# cart = {"Apple": 2, "Banana": 5, "Milk": 1}
# The user can add, remove, or update items.
# The program calculates the total price.
# 🔹 Bonus: Use a list of dictionaries to include prices and calculate the total bill

#product list to buy product
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "quantity": 5},
    {"id": 2, "name": "Smartphone", "price": 599.49, "quantity": 10},
    {"id": 3, "name": "Headphones", "price": 129.99, "quantity": 15},
    {"id": 4, "name": "Smartwatch", "price": 199.99, "quantity": 8},
    {"id": 5, "name": "Tablet", "price": 399.99, "quantity": 6}
]
shoppingCompleted = True
cartlist = [] #Cart list
while(shoppingCompleted):
    # input for id to buy products
    prodId = int(input("Enter a Product Id that you want to buy : "))
    #find the product via product id
    findProd = next((p for p in products if p["id"] == prodId),None)
    #check if product available or not
    if findProd:
        print(findProd)
        cartlist.append(findProd)
    else:
        print('No Product Found')
    # add confirmation for user if he want to add more product or not        
    confirmUser = input('You Want to add More (Yes or No):')
    # check yes or no
    if(confirmUser.lower() == "Yes".lower()):
        continue
    else:
    # sum of total price of cart items
        totalPrice = sum(product["price"] for product in cartlist)
        print("## Items , You have purchased ##")
        #print the item that user purchased
        for items in cartlist:
            print(f"{items["name"]} - {items["price"]}")

        ## total Cart Price
        print(f'Total Cart Price : {totalPrice}') 
        shoppingCompleted = False


#Question 08
# Create a traffic light simulation where:

# The user enters the current light color (Red, Yellow, Green).
# Use a single-line if-else (ternary operator) to decide the next action:
# "Stop" for Red
# "Slow Down" for Yellow
# "Go" for Green
# 🔹 Bonus: Add a random timer to simulate changing lights


#color for traffic signals

signalColor = input('Enter a Color :')

#add conditions
print("Stop") if signalColor.lower() == "red".lower() else print('Slow Down') if signalColor.lower() == "yellow".lower() else print('GO') if signalColor.lower() == "green".lower() else "Invalid Signal"


#Question 09

# Write a grading system where:

# The user enters a score (0-100).
# The program prints the grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# 🔹 Bonus: Do this in one line using a clever if-elif-else.

#user score
userScore = int(input("Enter Your Score (0 to 100):"))
#check user score and then show the grade according to the score
if userScore>=90 and userScore<=100:
    print('A')
elif userScore >=80 and userScore<=89:
    print('B')    
elif userScore >=70 and userScore <=79:
    print("C")    
elif userScore >=60 and userScore<=69:
    print("D")    
elif userScore<60:
    print("F")    
else:
    print('Invalid Score')