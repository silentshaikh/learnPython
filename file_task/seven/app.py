# Task 7: Find and Replace Words in a File
# 🔹 Write a program that:

# Reads a text file.
# Searches for a specific word and replaces it with another word.
# Saves the modified content in a new file.

#read the input file
readInputFile = open("input.txt","r")
textOfFile = readInputFile.read()
readInputFile.close()

#create a new file to save the text with replace value
outputFile = open("output.txt","w")
replaceTheText = textOfFile.replace("Python","Javascript")
outputFile.write(replaceTheText)
outputFile.close()