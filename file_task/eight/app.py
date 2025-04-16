import csv
# Task 8: Analyze a CSV File
# 🔹 Write a Python program that:

# Reads a CSV file containing student names and scores.
# Calculates the average score.
# Finds and prints the highest and lowest scores with student names.

readCsvFile = open("student.csv","r")
csvFile = csv.DictReader(readCsvFile)
print(csvFile)
averageScore = 0
totalScore = 0
lengthOfCsv = 0
maximumNum:int = float("-inf")
minimumNum = float("inf")
studentName = ""
lowestStudent = ""
for line in csvFile:
    for w in line:
        if  "score" in w.lower():
            studentScore = int(line.get(w)) 
            totalScore += studentScore
            print(line.get(w))
            lengthOfCsv+=1
            if studentScore > maximumNum:
                maximumNum = studentScore
                studentName = line.get("Name")

            if studentScore<minimumNum:
                minimumNum = studentScore
                lowestStudent = line.get("Name")

print(totalScore,lengthOfCsv)
averageScore = totalScore/lengthOfCsv
print("Average Score : ",averageScore)
print(f"Highest Score : {studentName} ({maximumNum})")
print(f"Lowest Score : {lowestStudent} ({minimumNum})")