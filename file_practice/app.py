import os
# File Handling Assignment (Python)

# 1️⃣ Basic File Operations
# 🔹 Write a Python program to:
# Create a new file "data.txt" and write the following text inside it:

# Python is a powerful programming language.
# It is widely used in web development, data science, and automation.
# Close the file and reopen it in read mode, then print its content.

fileCreate = open("data.txt","w")
fileCreate.write("Python is a powerful programming language.\n")
fileCreate.write("It is widely used in web development, data science, and automation.")
fileCreate.close()

# fileRead = open("data.txt","r")
# print(fileRead.read())
# fileRead.close()

# 2️⃣ Reading a File
# 🔹 Modify your program to read only the first line from the file "data.txt" and print it.
# readFistLine = open("data.txt","r")
# print(readFistLine.readline())
# readFistLine.close()


# 3️⃣ Appending Data to a File
# 🔹 Write a program that:

# Opens "data.txt" in append mode.

# Adds the following lines:

# Python supports multiple programming paradigms.
# It has a large standard library.
# Reopen the file in read mode and print all lines.

# appendDataFile = open("data.txt","a")
# appendDataFile.writelines(["\nPython supports multiple programming paradigms.\n","It has a large standard library.\n"])
# appendDataFile.close()
# readAppendFile = open("data.txt","r")
# print(readAppendFile.read())
# readAppendFile.close()


# 4️⃣ Writing Multiple Lines to a File
# 🔹 Write a Python program that:

# Creates a new file called "students.txt".
# Writes the names of 5 students (one name per line).
# Reads the file and prints all names as a list.
multiLineFile = open("students.txt","w")
multiLineFile.write("Sam\n")
multiLineFile.write("Tom\n")
multiLineFile.write("Jerry\n")
multiLineFile.write("Ben\n")
multiLineFile.write("Jack\n")
multiLineFile.close()

# readMultiLine = open("students.txt","r")
# print(readMultiLine.read())
# readMultiLine.close()


# 5️⃣ Counting Words in a File
# 🔹 Write a Python program that:

# Reads "data.txt".
# Counts and prints the number of words in the file.
# countWordFile = open("students.txt","r")
# countWord = 0
# for word in countWordFile.read():
#     if word.isalpha():
#         countWord+=1
    
# print(countWord)
# countWordFile.close()


# 6️⃣ Copying File Content
# 🔹 Write a Python program that:

# Reads the content of "data.txt".
# Creates a new file called "backup.txt".
# Copies all content from "data.txt" to "backup.txt".

# dataFileRead = open("data.txt","r")
# backUpFile = open("backup.txt","w")
# for line in dataFileRead.readlines():
#     backUpFile.write(line)

# dataFileRead.close()
# backUpFile.close()

# readBackUpFile = open("backup.txt","r")
# print(readBackUpFile.read())
# readBackUpFile.close()



# 7️⃣ File Pointer Operations (seek() and tell())
# 🔹 Write a Python program that:

# Opens "data.txt" in read mode.
# Moves the file pointer to the 10th character using seek().
# Prints the current cursor position using tell().
# Reads and prints the rest of the file.

# setFilePointer = open("data.txt","r")
# setFilePointer.seek(10)
# print(setFilePointer.tell())
# print(setFilePointer.read())
# setFilePointer.close()


# 8️⃣ Deleting a File
# 🔹 Write a Python program that:

# Checks if "backup.txt" exists.
# If it exists, delete the file using the os module.
# Print a message: "backup.txt deleted successfully" or "File does not exist".

# deleteBackupFile = open("backup.txt","r")
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
else:
    print("File does not exist")