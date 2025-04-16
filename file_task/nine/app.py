# Task 9: Split a Large File into Smaller Files
# 🔹 Write a Python program that:

# Reads a large text file.
# Splits it into smaller files, each containing N lines (user-defined).
# 📄 input.txt (Contains 1000 lines)
# ✅ Split into multiple files:

# part1.txt (Lines 1-100)
# part2.txt (Lines 101-200)

# Read the input file
with open("input.txt", "r") as readInputFile:
    textOfInput = readInputFile.readlines()

lines_per_file = 100  # Split each file into 100 lines
numForFile = 1        # Start with part1.txt
line_count = 0        # Line counter

# Loop through each line in input.txt
for line in textOfInput:
    # Open the correct part file and write the line
    with open(f"part{numForFile}.txt", "a") as newFile:
        newFile.write(line)

    line_count += 1  # Increment the line counter

    # If 100 lines have been written, start a new file
    if line_count == lines_per_file:
        numForFile += 1  # Move to next part file
        line_count = 0    # Reset counter for new file

print("✅ File splitting completed successfully!")

    