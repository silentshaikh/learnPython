# 🔹 Task 5: File Compression (Basic Run-Length Encoding)
# 🔹 Implement a simple Run-Length Encoding (RLE) compression algorithm:

# Read a text file.
# Compress it using RLE, where consecutive repeated characters are replaced by {count}{character}.
# Store the compressed text in "compressed.txt".
# Write a function to decompress the file back to its original form in "decompressed.txt".


# readFile = open("input.txt","r")
# textofFile = readFile.read()
# readFile.close()
# compress = ""
# for char in textofFile:
#     print(char)
#     countOfChar = textofFile.count(char)
#     if compress.find(char) == -1:
#     #     continue
#     # else:
#         compress += f"{countOfChar}{char}"

# #create a new file to save the compressed text
# print(compress)
# compressFile = open("compressed.txt","w")
# compressFile.write(compress)
# compressFile.close()

# # decompress the text
# readCompressFile = open("compressed.txt","r")
# textofCompress = readCompressFile.read()
# readCompressFile.close()
# #create a decompressed.txt file 
# decompressFile = open("decompressed.txt","w")
# #run a loop to set the decompressed data
# for num in range(0,len(textofCompress),2):
#     one = int(textofCompress[num])
#     two = textofCompress[num+1]
#     decompressFile.write(one*two)
# decompressFile.close()


#Another Solution

# 🔹 Run-Length Encoding (Compression)
def rle_compress(text):
    compressed = ""
    i = 0

    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compressed += f"{count}{text[i]}"
        i += 1

    return compressed


# 🔹 Run-Length Decoding (Decompression)
def rle_decompress(text):
    decompressed = ""
    i = 0

    while i < len(text):
        count = ""
        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1

        if i < len(text):
            decompressed += text[i] * int(count)
            i += 1

    return decompressed


# ✅ Read input file
with open("input.txt", "r") as file:
    original_text = file.read()

# ✅ Compress and save
compressed_text = rle_compress(original_text)
with open("compressed.txt", "w") as file:
    file.write(compressed_text)

# ✅ Decompress and save
decompressed_text = rle_decompress(compressed_text)
with open("decompressed.txt", "w") as file:
    file.write(decompressed_text)

# ✅ Print results
print("Original:", original_text)
print("Compressed:", compressed_text)
print("Decompressed:", decompressed_text)
