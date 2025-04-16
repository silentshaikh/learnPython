# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# num = 0
# while num<len(fruits):
#     print(fruits[num])
#     num+=1

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for mat in matrix:
#     for m in mat:
#         print(m,end="    ")
#     print()

# num2 = 0
# while num2<len(matrix):
#     num3 = 0
#     while num3<len(matrix[num2]):
#         print(matrix[num2][num3],end=" ")
#         num3+=1
#     print()
#     num2+=1

#enumerate() with list
# for index,mat in enumerate(matrix):
#     print(mat,index)


# #enumerate() with tuple
# for index,mat in enumerate((1,2,3,4,5,6,7)):
#     print(mat,index)

# #enumerate() with set
# for index in enumerate({1,2,3,4,5,6,7}):
#     print(index)

# obj = {"name":"Moiz"}
# # print(enumerate(obj.items()))
# #enumerate() with dictionary
# for index,(mat,mt) in enumerate(obj.items()):
#     print(mat,mt,index)


# #zip()
# names = ["Moiz", "Ali", "Sara"]
# ages = [25, 30, 22]

# zipped = zip(names, {12:"tv",13:"tt",14:"fr"})  # Creates pairs
# print(set(zipped))  # Convert to list
# for name,age in zip(names,{12:"tv",13:"tt",14:"fr"}):
#     print(name,age)


# List Comprehensions

numList = [1,2,3,4,5,6,7,8]
listComp = [num for num in numList if num%2==0]
listComp = ["even" if num%2==0 else "odd" for num in numList]
listComp = [(index,num) for index,num in enumerate(numList)]
print(listComp)