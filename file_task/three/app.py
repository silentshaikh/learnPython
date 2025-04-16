#  Task 3: Find the Most Frequent Word in a File
# 🔹 Write a program that:

# Reads a text file.

# Finds and prints the most frequently occurring word and its count.

readFileForCountWord = open("sample.txt","r")
ListOfFile = readFileForCountWord.read().split()
frequentlyWordCount = 0
frequentlyWord = ""
for word in ListOfFile:
    if ListOfFile.count(word)>frequentlyWordCount:
        frequentlyWordCount = ListOfFile.count(word)
        frequentlyWord = word

readFileForCountWord.close()
print(f"Most Frequent Word ({frequentlyWord}) : ",frequentlyWordCount)