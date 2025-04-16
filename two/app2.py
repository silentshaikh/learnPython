# List

numList = [1,2,3,4,5,6,7,8,11,10]
# numList[1:4] = [20,30]
print(numList)

#slicing
print("Slicing")
print(numList[2:]) #starting from 2 index
print(numList[:2])
print(numList[-4:-2])
print(numList[-5:-4])
print(numList[-4:])
print(numList[:-4])

#sling with steps
print(numList[::2])
print(numList[1::2])
print(numList[1:4:2])
print(numList[::3])

# List Methods & Functions in Python 

# print("List Methods & Functions")
# List Functions
# print(len(numList))
# print(max(numList))
# print(min(numList))
# print(sum(numList))
# print(sorted(numList))
# print(list("Hello"))
fruitList = ['apple','banana','watermelon',"cherry",'orange','kiwi']
# print(max(fruitList))
# # print(sum(fruitList))
# print(sum([1,2,3.4,5,6]))
# print(sorted(numList))
# print(sorted(numList,reverse=True))
# print(sorted(fruitList,key=len))

# listConv = list((1,))
# print(listConv)
# print(list("hello world"))
# print(list({12,34,56}))
# print(list({"a": 1, "b": 2, "c": 3}))

print("List Method")
# numList.append(True)
# numList.append([4,5])
# numList.append("Hello")
# numList.append(lambda x : x**2)
# print("Append",numList)

# numList.insert(0,45)
# numList.insert(-2,50)
# numList.insert(len(numList),60.34)
# numList.insert(23,"Hello")
# numList.insert(223,bool)
# print(numList)
# print(numList[13])

# numList.extend([9,10])
# numList.extend({60,70,80})
# numList.extend({"a": 1, "b": 2, "c": 3})
# numList.extend((1,))
# print(numList)
# print({1,2,3,4,5,6,7,8,9,34,56,80})

# numList.remove(4)
# print(numList)
# print(numList)
# print(numList.index(5,0,5))
# print(numList.count(bool))

# Sorting & Reversing
numArr = [1,3,4,5,6,2,8,7,100,400,250,120,80,23,45,15]
numArr.sort()
print(numArr)
numArr.sort(reverse=True)
print(numArr)

sports = ["cricket","football","Basketball","tennis","Wolly Ball", "Base Ball"]
sports.sort(key=len)
print(sports)

numbers = [-5, 3, -8, 1, -2]
numbers.sort(key=abs)  
print(numbers)  

boolList = [False,True,False,True]
boolList.sort()
print(boolList)

setList = [(1,2),(5,6),(3,4)]
setList.sort()
print(setList)

# Sorting by the Second Element in a Tuple
pairs = [(1, 3), (4, 1), (2, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)

#  Sorting by Absolute Value
abslouteList = [-5,3,-8,1,-2]
abslouteList.sort(key=abs)
print(abslouteList)

#  Sorting by Last Character of a String
print(fruitList)
fruitList.sort(key=lambda x:x[-1])
print(fruitList)

data = [{3, 1, 2}, {5, 4}, {7, 6}]
data.sort()  
print(data)  

# Copying
print("Copying : ")
arrCopy =  numArr.copy()
numArr[0] = 540
print(arrCopy)
print(numArr)