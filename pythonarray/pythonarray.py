# List is used to stora collection data like month or any kinds of lists

fruitArr = ["Apple","Banana","Orange","Kiwi"]
numList = [1,2,3,4,5]

print(len(fruitArr)) # return the length of list

# Slicing in List
copyFruit = fruitArr[0:2]
print(copyFruit)


# Sorting in List
fruitArr.sort()
print(fruitArr)

#List Methods

# append is used to add item at the end of list
fruitArr.append("Guava")
print("Append :",fruitArr)
# print(copyFruit)

# return a copy of the list
copyList = fruitArr.copy()
print("Copy :",copyList)

# return the number of element with a specific value
print("Count :",copyList.count("Apple"))

# return the index of the first element with a specific value
print("Index :",copyList.index("Apple"))

# add an item at a specific position
copyList.insert(0,"Cherry")
print("Insert :",copyList)

#remove an element at a specific position
copyList.pop(1)
print("Pop :",copyList)

#remove an item with a specific value
copyList.remove("Guava")
print("Remove",copyList)

# reverse the order of the list
copyList.reverse()
print("Reverse :",copyList)

# Sort the list
copyList.sort()
print("Sort :",copyList)

#Add the elements of a list (or any iterable), to the end of the current list 
copyList.extend(numList)
print("Extend :",copyList)

#clear all the item from the list
fruitArr.clear()
print("Clear :",fruitArr)

