# Dictionary Assignments for Practice

# 1️⃣ Basic Dictionary Operations
# Create a dictionary student with keys: name, age, grade, and city. Assign any values.
# Print the value of age using key lookup.
# Add a new key-value pair: email: 'example@gmail.com'.
# Update the value of city to a different city.
# Remove the key grade using .pop().
# Print the final dictionary.

person = {
    'name':'Sam',
    'age':20,
    'grade': 'A',
    'city':'Washington'
}

print(person['age'])
person['email'] = 'sam@gmail.com'
person['city'] = 'VA'
person.pop('grade')
print(person)


# 2️⃣ Dictionary Methods Practice
# Write a program that:

# Creates a dictionary product = {'name': 'Laptop', 'price': 1000, 'stock': 5}.
# Uses .get() to safely retrieve the price.
# Uses .setdefault() to add a default key discount with a value of 10%.
# Uses .keys(), .values(), and .items() to print all keys, values, and key-value pairs.
# Uses .update() to change the price to 900.
# Uses .clear() to empty the dictionary.
product = {'name': 'Laptop', 'price': 1000, 'stock': 5}
print(product.get('price'))
product.setdefault("discount",400)
print(product)
print(product.keys())
print(product.values())
print(product.items())
product.update({'price':400})
print(product)
product.clear()
print(product)


# 3️⃣ Counting Word Frequency (Intermediate Level)
# Write a Python program that:

# Takes a sentence as input from the user.
# Counts how many times each word appears in the sentence.
# Stores the result in a dictionary.
# Prints the dictionary.


# sentence = input("Enter a Sentence :").strip()
# sentList = sentence.split()
# print(sentList)
# senObj = {}
# for sen in sentList:
#     senCount = sentList.count(sen)
#     senObj[sen] = senCount

# print(senObj)


# 4️⃣ Student Marks Manager (Advanced Challenge)
# Create an empty dictionary called marks.
# Ask the user how many students they want to enter.
# For each student, ask for their name and marks. Store them in the dictionary.
# After all entries, print:
# The dictionary.
# The student with the highest marks.
# The student with the lowest marks.

# mark = {}
# isTrue = True
# while isTrue:
#     userName = input("Enter a Name : ")
#     userMarks = int(input('Enter a Marks : '))
#     mark[userName] = userMarks

#     more = input('You want more : ')
#     if more == 'no':
#         break
#     else:
#         continue

# print(mark)

# minValue = min(mark.values())
# minresult = [key for key in mark if mark[key] == minValue]
# maxValue = max(mark.values())
# maxresult = [key for key in mark if mark[key] == maxValue]
# print(f"Lowest Value : {mark[minresult[0]]}")
# print(f"Highest Value : {mark[maxresult[0]]}")



# 💡 Bonus Challenge (For Experts!)
# Write a Python program that:

# Creates a dictionary where keys are numbers from 1 to 10, and values are their squares.
# Converts the dictionary to a list of tuples.
# Sorts the dictionary by values (squares).
# Converts it back to a dictionary and prints it.


newDict = {}
for num in range(1,11):
    newDict[num] = num**2
print(newDict)
# dictionary into list of tuples
listOfTuple = list(newDict.items())
print(listOfTuple)
#sorted by squares
sortBySquare = sorted(newDict.items() , key=lambda item:item[1])
print(sortBySquare)
#convert into dictionary again
convIntoDict  = dict(sortBySquare)
print(convIntoDict)