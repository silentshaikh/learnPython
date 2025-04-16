# 📝 Assignment 1: Copy an Image File
# 📌 Task: Write a Python program to copy an image file (e.g., photo.jpg) using binary mode.
# ✅ Hint: Use "rb" (read binary) and "wb" (write binary).

# 🔹 Expected Output:
# The new image file (copied_photo.jpg) should be an exact duplicate of photo.jpg.

with open("Raw_App_Screenshot.png","br") as readImage:
    ourImg = readImage.read()

with open("copy.png","bw") as writeImg:
    writeImg.write(ourImg)

# 📝 Assignment 2: Read First 100 Bytes of a PDF
# 📌 Task: Open a PDF file in "rb" mode and read the first 100 bytes.
# ✅ Hint: Use .read(100) to extract the first 100 bytes.

# 🔹 Expected Output:
# The console should print the first 100 bytes (which may look like random characters).
with open("Sets Internal Working.pdf","br") as readPdf:
    print(readPdf.read(100))


# 📝 Assignment 3: File Backup System
# 📌 Task: Create a Python script that automatically creates a backup copy of a file (any type).
# ✅ Steps to Follow:

# Ask the user to enter a file name (e.g., data.pdf).
# Copy the file and save it as backup_data.pdf.
with open("Sets Internal Working.pdf","br") as readPdfFile:
    myPdf = readPdfFile.read()

with open("backup_file.pdf","bw") as backUpFile:
    backUpFile.write(myPdf)


# 📝 Assignment 4: Write and Read Binary Data
# 📌 Task: Write a Python script to:

# Write a byte sequence (b'\x41\x42\x43\x44') to a binary file (data.bin).
# Read and print the contents of data.bin in "rb" mode.
# ✅ Hint: b'\x41' is the binary representation of "A", so b'\x41\x42\x43\x44' = "ABCD".
with open("fontawesome-webfont.bin","br") as readBinary:
   binaryData = readBinary.read()

with open("copy.bin","bw") as writeBinary:
    writeBinary.write(b'\x41\x42\x43\x44')

with open("copy.bin","br") as binaryRead:
    dataBin = binaryRead.read()
    decodeData = dataBin.decode("utf-8") #bytes to string
    print(decodeData)


# 📝 Assignment 5: Split a Large File into Chunks
# 📌 Task: Write a Python script to split a large file (e.g., video.mp4) into smaller chunks (e.g., chunk_1.mp4, chunk_2.mp4, etc.).
# ✅ Steps to Follow:

# Open the file in "rb" mode.
# Read 100KB at a time.
# Save each chunk as a separate file.
# 🔹 Hint: Use .read(102400) to read 100KB chunks.

with open("0426.mp4", "rb") as readVideo:  # 'rb' (not 'br')
    count = 1
    while True:
        ourVideo = readVideo.read(10485760)  # Read 10MB chunk
        if not ourVideo:  # Stop when no more data
            break
        with open(f"chunk{count}.mp4", "bw") as chunkFile:  # Use 'wb' to write binary
            chunkFile.write(ourVideo)
        print(f"Created chunk{count}.mp4")
        count += 1

print("Splitting complete!")

with open("Quarter3.pdf","br") as appendFile:
    quartrCard =  appendFile.read()

with open("backup_file.pdf","ab") as addDataPdf:
    addDataPdf.write(quartrCard)

with open("wor.txt","rb") as readBinry:
    print(readBinry.read())

with open("wor.txt","ab") as appendBinary:
    appendBinary.write(b"loremipsum")

with open("readandwrite.txt","br+") as readAndWrite:
    readAndWrite.write(b"lorem ipsum")
    readAndWrite.write(b"Hello World")

with open("readandwrite.txt","br+") as readAndWrite2:
    readAndWrite2.write(b"Harry Potter")


with open("writeandread.txt","bw+") as writeAndRead:
     writeAndRead.write(b"lorem ipsum")
     writeAndRead.write(b"Hello World")

with open("writeandread.txt","bw+") as writeAndRead2:
    writeAndRead2.write(b"Harry Potter")