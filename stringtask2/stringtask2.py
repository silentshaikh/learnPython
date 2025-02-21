
# Question #01
# Write a program that takes a sentence and removes all duplicate words while preserving the order
"""
sentence = input("Enter a Sentence : ")
if not sentence:
    print("Plz Enter a Sentence")
else:
    senArr = sentence.split()
    uniqueWords =[]
    seen = set()
    for sen in senArr:
        if sen not in seen:
            uniqueWords.append(sen)
            seen.add(sen)
    result = " ".join(uniqueWords)        
    print(result)
"""


# Question 02
# Write a program that finds the most frequently occurring character in a given string (excluding spaces).
# 🔹 Bonus: If there are multiple characters with the same frequency, return the first one that appears.
"""
word = input("Enter a Word : ").replace(" ","")
if not word:
    print("Plz Enter a Word")
else:
    freq = {}  # Dictionary to store character frequency
    for w in word:
        freq[w] = freq.get(w,0)+1 # Count occurrences
    maximumCharacter = max(freq,key=freq.get) # Get the character with the highest count
    print(f"The most frequent character is: '{maximumCharacter}' (Appeared {freq[maximumCharacter]} times)")    
"""

# Question 03
# Write a program that reverses only the words with even lengths in a sentence, keeping odd-length words unchanged.
"""
sentence = input("Enter a Sentence : ")
if not sentence:
    print("Plz Enter a Sentence")
else:
    senArr = sentence.split()
    reverseSenArr = []    
    print(senArr)
    for sen in senArr:
        if len(sen) %2 ==0:
            reverseSen = sen[::-1]
            reverseSenArr.append(reverseSen)
        else:
            reverseSenArr.append(sen)    
    print(reverseSenArr)        
"""


# Question 04
# Write a program that shifts each letter in a string forward by 3 positions in the alphabet.

# 'a' → 'd', 'b' → 'e', ..., 'x' → 'a', 'y' → 'b', 'z' → 'c'.
# Spaces remain unchanged.

"""
userMessage = input("Enter a Message : ").replace(" ","")
if not userMessage:
    print("Plz Enter a Message")
else:
    forwardBy3 = ""    
    for character in userMessage:
        if character.isalpha: # Only shift letters
            newCharacter = chr(ord(character)+3) # Shift by 3 places
        else:
            newCharacter = character;   # Keep non-alphabetic characters unchanged 
        forwardBy3 += newCharacter
    print("Shifted Character By 3 : "+forwardBy3)        
"""
"""
userMessage = input("Enter a Message: ").replace(" ", "")

if not userMessage:
    print("Plz Enter a Message")
else:
    forwardBy3 = ""
    
    for character in userMessage:
        if character.isalpha():
            if character.islower():
                new_char = chr((ord(character) - 97 + 3) % 26 + 97)  # Wrap a-z
            else:
                new_char = chr((ord(character) - 65 + 3) % 26 + 65)  # Wrap A-Z
        else:
            new_char = character  # Keep non-alphabetic characters unchanged

        forwardBy3 += new_char

    print("Shifted Message:", forwardBy3)
"""

# Question 05
# Write a program that takes a sentence and counts how many times each word appears
"""
countWords = input("Enter a Sentence : ")
if not countWords:
    print("Enter a Sentence")
else:
    wordsArr = countWords.split()
    wordObj = {}    
    for word in wordsArr:
        wordObj[word] = wordObj.get(word,0)+1
    for w in wordObj:
        print(f"{w} - {wordObj[w]}")    
"""

# Question 06

# Write a program that finds the first character in a string that does not repeat
"""
strWord = input("Enter a Word : ")
if not strWord:
    print("Plz Enter a Word")
else:
    onlyOne = {}
    for w in strWord:
        onlyOne[w] = onlyOne.get(w,0)+1
    minimumCharacter = min(onlyOne,key=onlyOne.get)
    print(f"First Non-Repeating Character is : {minimumCharacter}")    
"""

#Question 07

# Write a program that checks if two strings are rotations of each other.
"""
strOne = input("Enter First String : ")
strTwo = input("Enter Second String : ")
if not strOne or not strTwo:
    print("Plz Enter the strings")
elif len(strOne)  != len(strTwo): 
    print("Length are different")   
else:
   if strTwo in (strOne + strOne):
    print("Yes, this string are rotation of each other")
   else:
    print("No, the strings are not rotations.") 
"""

# Question 08
# Write a program that converts a number (1-999) into words.
"""
def number_to_words(n):
    if n < 1 or n > 999:
        return "Please enter a number between 1 and 999"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    words = ""

    # Handle hundreds place
    if n >= 100:
        words += ones[n // 100] + " Hundred"
        n %= 100
        if n > 0:
            words += " and "

    # Handle tens and ones place
    if 10 <= n <= 19:
        words += teens[n - 10]
    else:
        words += tens[n // 10]
        if n % 10 > 0:
            words += " " + ones[n % 10]

    return words.strip()

# Get user input
convNumIntoWord = int(input("Enter a Number (1-999): "))
print(number_to_words(convNumIntoWord))
"""

# Question 09

# Write a program that reverses only the letters in a string, leaving numbers and symbols in place
"""
def reverseLetter(letter):
    letters = [char for char in letter if char.isalpha()] # Extract Only Letter
    result = []
    letterIndex = len(letters)-1 # start from the last letter
    for char in letter:
        if char.isalpha():
            result.append(letters[letterIndex]) # replace letter with reversed one
            letterIndex -=1
        else:
            result.append(char)
    return "".join(result)            

reverseOnlyStr = input("Enter a Word : ")
if not reverseOnlyStr:
    print("Plz Enter a Word")
else:
    print(reverseLetter(reverseOnlyStr))
    # reverseStr = ""
    # for w in reverseOnlyStr:
    #     if w.isalpha():
    #         reverseStr += w
"""


#Question 10

#Write a program that finds the longest palindromic substring in a given string.

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]  # Return the palindrome found

def longest_palindromic_substring(s):
    if len(s) == 0:
        return "Plz Enter a Word"

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        odd_palindrome = expand_around_center(s, i, i)
        # Even-length palindrome (two character center)
        even_palindrome = expand_around_center(s, i, i + 1)

        # Compare and update longest palindrome
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

# Get user input
palindrome_str = input("Enter a Word: ").replace(" ", "")
if not palindrome_str:
    print("Plz Enter a Word")
else:
    print("Longest Palindromic Substring:", longest_palindromic_substring(palindrome_str))

