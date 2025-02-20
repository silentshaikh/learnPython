import re
# Question 01

# Write a program that asks the user for their full name and:

# Converts the first letter of each word to uppercase.
# Removes any extra spaces.
# Displays the formatted name.
"""
userName = input("Enter your full Name : ")
print("Name : "+userName.title().strip())
"""

#Question 02
# Write a program that takes a sentence from the user and reverses the order of words, but not the letters inside words.

"""
sentence = input("Enter a Sentence : ")
if sentence :
   senArr = ' '.join(reversed(sentence.split(' '))) 
   print(senArr)
   print("Bonus : ",sentence[::-1])
else:
    print('Plz Enter a sentence')    
"""



#Question 03

# Create a password validator that checks if a password:
# ✔️ Has at least 8 characters
# ✔️ Contains at least one uppercase letter
# ✔️ Contains at least one digit
# ✔️ Contains at least one special character (@, #, $, etc.)

"""
passInput = input('Enter your Password : ')
validatePassword = re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\$\@\#\&])[A-Za-z\d\$\@\#\&]{8}$",passInput)
if passInput == "":
    print('Plz Enter a Password')
else:
    if len(passInput) > 8 or len(passInput) < 8:
        print('Plz Enter only 8 character')
    else:
        if validatePassword:
            print('Strong Password : ', passInput)    
        else:
            print('Weak Password : ', passInput)      
"""

# Question 04
# Write a program that generates a personalized email using f-strings or .format().

# Ask for name, age, and favorite hobby.
# Print a message using these details.

# userName = input("Enter your Name :")
# userAge = input("Enter your Age :")
# userSkill = input("Enter your Skill : ")

# personalizedMessage = f""" Dear {userName.title()}, 
# We hope you are having a Fantastic Day ! At the Age of {userAge}. {userSkill} is a fantastic skill to grow up in your career and for future also , so best of luck."""
# if not userName or not userAge or not userSkill:
#     print("Enter Your Name, Age and Skill")
# else:
#     print(personalizedMessage)    

# Question 05

# Write a program that:

# Takes a sentence and a word to find from the user.
# Checks if the word exists in the sentence.
# If found, print its position (index).

"""
sentenceforFind = input("Enter a Sentence : ")
findWord = input('Enter a Word to find fron the sentence :')
if not sentenceforFind:
    print("Plz Enter a Sentence")
else:
    if not findWord:
        print("Plz Enter a Word to find fron the sentences")
    else:
        findtheWord = sentenceforFind.lower().find(findWord.lower())
        if  findtheWord<0:
            print(f"Here we have no word like this {findWord}")  
        else:
            print(f'The Word has Found Successfully and the Position is : {findtheWord}')         
"""

# Question 06
# Write a program that checks if a given word is a palindrome (reads the same forward and backward).
"""
checkPalindrome = input("Enter a Word :").strip().replace(' ','')
if not checkPalindrome:
    print("Plz Enter a word")
else:
    palidrome = checkPalindrome[::-1]
    print(palidrome)    
    if checkPalindrome == palidrome:
        print("Yes, it's a Palindrome")
    else:
        print("It's not a Palindrome")    
"""


# Question 07
# Write a program that counts the number of vowels (a, e, i, o, u) and consonants in a given sentence.        

"""
countWord = input("Enter a Word :")
vowels = []
consonent = []
if not countWord:
    print("Plz Enter a Word")
else:
    for word in countWord:
        if(word == "a" or word == "e" or word == "o" or word == "i" or word == "u"):
            vowels.append(word)
        else:
            consonent.append(word)

    print("Vowels : " ,len(vowels))        
    print("Consonents : ",len(consonent))
"""

#Question 08

# Write a program that checks if two words are anagrams (contain the same letters in a different order).
"""
firstWord = input("Enter a Word : ")
secondWord = input("Enter a Word : ")
if not firstWord or not secondWord:
    print('Plz Enter a Word')
else:
    if len(firstWord) == len(secondWord):
        print('Yes, they are anagrams')
    else:
        print("they are not anagrams")   
"""