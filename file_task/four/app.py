# 🔹 Task 4: Reverse a File Line-by-Line
# 🔹 Write a program that:

# Reads a text file line by line.

# Writes the lines in reverse order to a new file "reversed.txt".

# fileForReverse = open("input.txt","r")
# ourStr = fileForReverse.read().replace("\n"," ").replace(" ","")
# newStr =""
# for num in range(len(ourStr)):
#     if ourStr[num].isnumeric():
#         newStr += ourStr[num]
#         newStr+=" "
#     else:
#         newStr +=ourStr[num]

# print(newStr)
# reverseList = newStr.split()
# reverseList.reverse()
# print(reverseList)
# fileForReverse.close()
# #crreate a file for save the reverse list
# newReverxeFile = open("reversed.txt","w")
# for item in reverseList:
#     newReverxeFile.write(f"{item}\n")
# newReverxeFile.close()

# # #Read the Reversed File
# reversedFile = open("reversed.txt","r")
# print(reversedFile.read())



# Read the file line by line and store in a list
with open("input.txt", "r") as fileForReverse:
    lines = fileForReverse.readlines()

# Reverse the list of lines
reversed_lines = lines[::-1]
print(reversed_lines)

# Write the reversed lines to a new file
with open("reversed.txt", "w") as newReverseFile:
    newReverseFile.writelines(reversed_lines)

# Read and print the reversed file
with open("reversed.txt", "r") as reversedFile:
    print(reversedFile.read())
