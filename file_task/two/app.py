# Task 2: Merge Two Sorted Files
# 🔹 Write a program that:

# Takes two text files ("file1.txt" and "file2.txt") containing sorted numbers (one per line).

# Merges them into a single sorted file called "merged.txt".

fileOne = open("file1.txt","r")
fileTwo = open("file2.txt","r")
oneAndTwo = sorted(map(int,fileOne.read().split() + fileTwo.read().split()))
fileOne.close()
fileTwo.close()
mergedFile = open("merged.txt","w")
# print(oneAndTwo)
for num in oneAndTwo:
    mergedFile.write(f"{num}\n")

mergedFile.close()

readMerged = open("merged.txt","r")
print(readMerged.read())
readMerged.close()
