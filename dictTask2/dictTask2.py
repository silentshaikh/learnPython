import random
import string
from collections import defaultdict



# 1️⃣ Nested Dictionary - Employee Records
# Write a Python program that:
# Creates a dictionary employees, where each key is an employee ID, and the value is another dictionary containing:
# name: Employee’s name
# salary: Employee’s salary
# department: Employee’s department
# Allow the user to:
# Add new employees
# Update an employee’s salary
# Delete an employee by ID
# Find employees with the highest and lowest salary

# employess = {}
# isTrue = True
# def findEmpSalary():
#    if not employess:
#        print("No Employee is here") 
#        return
#    highestEmpSalary = max(employess.items(), key=lambda emp:emp[1]['salary']) 
#    lowestEmpSalary = min(employess.items(), key=lambda emp:emp[1]['salary']) 
#    print(f"\nEmployee with the Highest Salary: {highestEmpSalary[1]['name']} (${highestEmpSalary[1]['salary']})")
#    print(f"Employee with the Lowest Salary: {lowestEmpSalary[1]['name']} (${lowestEmpSalary[1]['salary']})")
# while(isTrue):
#     def generate_unique_id(length=5):
#         characters = string.ascii_uppercase + string.digits
#         return ''.join(random.choice(characters) for _ in range(length))

# # Example usage
#     unique_id = generate_unique_id().lower()
#     print(unique_id)
#     name = input("Enter a Name : ")
#     salary = int(input("ENter a salary : "))
#     department = input("Enter a deparment")
#     employess[unique_id] = {'name':name,'salary':salary,'department':department}
#     moreEmp = input("You want to add more (yes | no) :")
#     if moreEmp == 'no':
#         while True:
#             print('1) Remove an Employee \n 2) Update an Employee \n 3)Find Salary Extremes \n 4) Exit')
#             options = input("Choose an Option :")
#             if options.lower() == '1'.replace(" ",'').lower():
#                 removeEmp = input("Enter an ID to remove the Emplyee : ")
#                 if removeEmp in employess:
#                     employess.pop(removeEmp.lower())
#                 else:
#                     print("ID is not available")
#                 # 
#             elif options.lower() == '2'.replace(" ",'').lower():
#                 updateEmp = input("Enter an ID to update the Employee : ")
#                 if updateEmp in employess:
#                     listOfKeys = list(employess.keys())

#                     if updateEmp:
#                         updName = input('Update the Name : ')
#                         updSalary = int(input("Update the Salary : "))
#                         updDepartment = input("Update the Department : ")
#                         if updName and updDepartment and updSalary:
#                             employess[updateEmp] = {'name':updName,'salary':updSalary,'department':updDepartment}
#                         elif updName:
#                             employess[updateEmp]['name'] = updName
#                         elif updSalary:
#                             employess[updateEmp]['salary'] = updSalary
#                         elif updDepartment:
#                             employess[updateEmp]['department'] = updDepartment
#                     else:
#                         print('Plz Enter the name, salary, department')
#                 else:
#                     print("ID is not available")
#             elif options.lower() == '3'.replace(" ",'').lower():
               
#                 findEmpSalary()
#             elif options.lower() == '4'.replace(" ",'').lower():
#                  print('Exiting Program')
#                  exit()
#             else:
#                 print("Invalid option. Please choose again.")
                
# print(employess)   


# 2️⃣ Letter Frequency Counter (With Sorting)
# Write a function that:

# Takes a sentence as input.
# Counts how many times each letter appears in the sentence (ignore spaces).
# Returns a dictionary where keys are letters and values are their frequencies.
# Sort the dictionary by the frequency in descending order.

# sentence = input('Enter a Sentence : ').replace(" ",'')
# senObj = {}
# for sen in sentence:
#     senCount = sentence.count(sen)
#     senObj[sen] = senCount

# print(senObj)



# 3️⃣ Find the Most Repeated Word in a Paragraph
# Write a Python program that:

# Takes a paragraph as input.
# Counts how many times each word appears.
# Finds and prints the most repeated word along with its count.

# sentenceWord = input("ENter a Sentence : ")
# senList = sentenceWord.split()
# print(senList)
# count = 0
# word = ''
# for sen in senList:
#     if senList.count(sen)>count:
#         count  = senList.count(sen)
#         word = sen
# print(f"Most repeated word: {word} ({count} times)")



# 4️⃣ Anagram Groups (Group Words with Same Letters)
# Write a function that:

# Takes a list of words.
# Groups words that are anagrams together.
# Returns a dictionary where:
# Keys are sorted versions of the words
# Values are lists of anagrams

# def anagramGroup(lists):
#     anagrams = defaultdict(list)
#     print(anagrams)
#     for word in lists:
#         sortedWord = "".join(sorted(word))
#         anagrams[sortedWord].append(word)
#     return dict(anagrams)
# print(anagramGroup(["listen", "silent", "enlist", "eat", "tea", "ate"]))



# 5️⃣ Merge Two Dictionaries (With Summation of Common Keys)
# Write a function that:

# Takes two dictionaries where keys are product names and values are quantities sold.
# Merges the dictionaries.
# If a product exists in both, add the quantities together.

# sales1 = {'apple': 10, 'banana': 5, 'grapes': 8}
# sales2 = {'banana': 3, 'apple': 6, 'mango': 7}
# for sale in sales1:
#     if sale in sales2:
#         sales2[sale] += sales1[sale]
#     else:
#         sales2[sale] = sales1[sale]

# print(sales2) 


# def mergedDict(sales1:dict,sales2:dict):
#     mergedObj = {}
#     # Get all the unique keys
#     for product in set(sales1.keys()).union(sales2.keys()):
#         mergedObj[product] = sales1.get(product,0)+sales2.get(product,0)
#     return mergedObj

# print(mergedDict(sales1,sales2))



# 6️⃣ Reverse a Dictionary (Keys as Values, Values as Keys)
# Write a function that:

# Takes a dictionary where keys are words and values are meanings.
# Returns a new dictionary where keys and values are swapped.
# If multiple keys have the same value, store them as a list in the reversed dictionary.

# def reverseDictionary(ourDict:dict):
#     reverseDict= {}
#     # Iterate over each key, value pair in the original dictionary
#     for key, value in ourDict.items():
#         # Check if the value already exists as a key in reverseDict
#         if value in reverseDict:
#             # If the existing value is not a list, convert it into a list
#             if not isinstance(reverseDict[value],list):
#                 reverseDict[value] =  [reverseDict[value]]
#                 # Append the current key to the list
#                 reverseDict[value].append(key)
#         else:
#             # Otherwise, just assign the key to this value
#             reverseDict[value] = key
#     return reverseDict

# print(reverseDictionary({'fast': 'quick', 'rapid': 'quick', 'big': 'large', 'huge': 'large'}))


# 7️⃣ Deepest Key Finder in a Nested Dictionary
# Write a function that:

# Takes a deeply nested dictionary as input.
# Finds and returns the deepest key along with its depth level


#finding depth
def deepKeyFind(ourDict:dict,depth=1):
       """
    Recursively traverse the dictionary and return a list of (key, depth) tuples.
    """
       ourResults = []
       for key,value in ourDict.items():
              ourResults.append((key,depth))
              if isinstance(value,dict):
                     ourResults.extend(deepKeyFind(value,depth+1)) 

       return ourResults
    

#finding deep key
def deepKey(ourDict:dict):

    """
    Find and return the deepest key and its depth from a nested dictionary.
    """
    allKeys = deepKeyFind(ourDict)
    if not allKeys:
          return None,0
    # Return the key with the maximum depth.
    return max(allKeys,key=lambda x:x[1])

dictDeepest, dictDepth = deepKey({
    'a': {'b': {'c': {'d': {'e': 'value'}}}}
})
print(f"Deepest Key : {dictDeepest}, at depth : {dictDepth}")