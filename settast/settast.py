import string,random
# # 1️⃣ Basic Set Operations
# # ✅ Task: Create two sets and perform the following operations:

# # Add an element to a set.
# # Remove an element from a set.
# # Check if an element exists in a set.
# # Find the length of a set.

# mySet = {1,2,3,4,5,6}
# # mySet.add(7)
# # mySet.remove(5)
# # print(3 in mySet)
# # print("Length : ",len(mySet))
# # print(mySet)


# # 2️⃣ Set Methods Practice
# # ✅ Task: Create two sets and use update(), clear(), and copy() methods.
# set2 = {7,8,9,10,11,12}
# # set2.update("12",mySet)
# # print("Update : ",set2)

# # setCopy = set2.copy()
# # print("Copy : ",setCopy)

# # set2.clear()
# # print("Clear : ",set2)


# # 3️⃣ Set Operations (Union, Intersection, Difference)
# # ✅ Task: Create two sets and perform:

# # Union
# # Intersection
# # Difference
# # Symmetric Difference
# setUnion = mySet.union(set2)
# print("Union : ",setUnion)
# setIntersection = mySet.intersection(set2)
# print("Intersection : ",setIntersection)
# setDifference = mySet.difference(set2)
# print("Difference : ",setDifference)
# setSymmetric = mySet.symmetric_difference(set2)
# print("Symmetric Difference : ",setSymmetric)


# # 4️⃣ Set Relations (Subset & Superset)
# # ✅ Task: Check if a set is a subset or superset of another.
# print("issubset : ",mySet.issubset(set2))
# print("issuperset : ",mySet.issuperset(set2))


# # 5️⃣ Disjoint Sets
# # ✅ Task: Check if two sets are disjoint (have no common elements).
# print("isdisjoint : ",mySet.isdisjoint(set2))


# # 6️⃣ Modify Set with symmetric_difference_update()
# # ✅ Task: Modify a set using symmetric_difference_update().
# mySet.symmetric_difference_update(set2)
# print("symmetric_difference_update()",mySet)


# # 7️⃣ Build a Unique List Using Sets
# # ✅ Task: Convert a list with duplicate values into a set to remove duplicates.
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# listIntoSet = set(numbers)
# print("List into Set",listIntoSet)


# # 8️⃣ Set-Based Word Filter
# # ✅ Task: Write a program that takes a sentence and removes duplicate words using a set.
# sentence = "Python is fun and Python is powerful"
# strIntoSet = set(sentence)
# print("String into Set",strIntoSet)




# 🔥 Advanced Set Assignments (Difficult Level) 🔥

# 1️⃣ Find Common Elements in Multiple Sets
# ✅ Task: Given three sets, find the common elements present in all of them.
# set1 = {10, 20, 30, 40, 50}
# set2 = {20, 30, 60, 70}
# set3 = {10, 20, 30, 80}

# commomElement = set1.intersection(set3,set2)
# print("Commom Elements :",commomElement)


# 2️⃣ Remove Elements Present in Another Set
# ✅ Task: Remove all elements from setA that are also in setB, without using loops.
# setA = {1, 2, 3, 4, 5, 6, 7}
# setB = {3, 4, 5}
# removeElement = setA.difference(setB)
# print("Remove Element : ",removeElement)


# 3️⃣ Set-Based Password Generator
# ✅ Task: Write a program that generates a random password using sets.

# It should include letters, numbers, and symbols.
# It should have no duplicate characters.

# def passwordGenerator():
#     passLetter = string.ascii_letters
#     passDigit = string.digits
#     pasSymbol = string.punctuation
#     ourPassword = passLetter+passDigit+pasSymbol
#     passwordSet:set = set()
#     while len(passwordSet) <= 8:
#         passwordSet.add(random.choice(ourPassword))
#     return passwordSet


# print(passwordGenerator())


# 4️⃣ Find Unique Elements Across Sets
# ✅ Task: Given three sets, find elements that are unique to each set (i.e., elements that appear in only 
# one set)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {6, 7, 8, 9}
# uniontheElement = set1.union(set2,set3)
# print(uniontheElement)
# commonElem = (set1&set2) | (set2&set3) | (set1&set2)
# print(commonElem)
# uniqueElem = uniontheElement.symmetric_difference(commonElem)
# print("Unique Element : ",uniqueElem)


# 5️⃣ Create a Set-Based Student Attendance System
# ✅ Task: Simulate a student attendance system using sets.

# present_students contains names of students who attended class.
# total_students contains all students enrolled.
# Find absent students.

# total_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
# present_students = {"Alice", "Charlie", "Eve"}
# absentStudent = total_students.difference(present_students)
# print("Absent Student : ",absentStudent)


# 6️⃣ Check If Two Words Are Anagrams Using Sets
# ✅ Task: Write a program that checks if two words are anagrams using sets.
# word1 = "listens"
# word2 = "silents"

# wordToSet1 = set(word1)
# wordToSet2 = set(word2)

# isAnagram = False
# for w in wordToSet1:
#     if len(word1) == len(word2):
#         if w in wordToSet2:
#             isAnagram = True
#         else:
#             isAnagram = False
#     else:
#         isAnagram = False

# if isAnagram:
#     print("They are Anagrams")
# else:
#     print("They are not the Anagrams") 

# from collections import Counter

# def are_anagrams(word1, word2):
#     # Step 1: Check if they contain the same unique letters
#     if set(word1) != set(word2):
#         return False

#     # Step 2: Check if they have the same frequency of each letter
#     return Counter(word1) == Counter(word2)

# # Example Usage
# word1 = "listens"
# word2 = "silents"

# if are_anagrams(word1, word2):
#     print("They are Anagrams")
# else:
#     print("They are not Anagrams")



# 7️⃣ Count Distinct Elements in a List Using Sets
# ✅ Task: Given a large list, find the number of unique elements using a set.
# numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 8, 9, 10, 10]
# numListIntoSet = len(set(numbers))
# print("Length : ",numListIntoSet)
# numListIntoSet = set()
# for num in numbers:
#     numCount = numbers.count(num)
#     if numCount>0 and numCount<2:
#         numListIntoSet.add(num)

# print(numListIntoSet)


# 8️⃣ Create a Word Frequency Counter Using Sets
# ✅ Task: Write a program that counts how many times each word appears in a sentence.
# sentence = "hello world hello python world python python".replace(",.",'')
# senIntoList = sentence.split()
# wordSet = set()
# for word in senIntoList:
#     wordCount = senIntoList.count(word)
#     # senObj[word] = wordCount
#     wordSet.add((word,wordCount))

# print(wordSet)


# 9️⃣ Find the Largest Common Subset in a List of Sets
# ✅ Task: Given multiple sets, find the largest subset common to all sets.

set_list = [
    {1, 2,3,4},
    {2, 3, 4, 5},
    {3, 4, 6, 7},
    {3, 4, 8, 9}
]
maxOfSet = set_list[0]
for sets in set_list:
    maxOfSet = maxOfSet.intersection(sets)

if len(maxOfSet) >0:
    print(maxOfSet)
else:
    print("No Largest Common")


# 🔟 Remove Stopwords from a Text Using Sets
# ✅ Task: Remove common stopwords (like "is", "the", "and") from a given sentence.
# text = "Python is the best programming language and it is powerful"
# stopwords = {"is", "the", "and", "it"}
# removeCommonStopWords = ''
# for word in stopwords:
#   if removeCommonStopWords:
#       removeCommonStopWords = removeCommonStopWords.replace(word,'')
#   else:
#        removeCommonStopWords = text.replace(word,'')

# print(removeCommonStopWords)

# def remove_stopwords(text, stopwords):
#     words = text.split()  # Split text into words
#     filtered_words = [word for word in words if word.lower() not in stopwords]  # Remove stopwords
#     return " ".join(filtered_words)  # Join back into a sentence

# # Example
# text = "Python is the best programming language and it is powerful"
# stopwords = {"is", "the", "and", "it"}

# filtered_text = remove_stopwords(text, stopwords)
# print(filtered_text)