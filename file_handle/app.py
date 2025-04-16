# oneFile = open("abc.txt","w")
# # print(oneFile)
# oneFile.write("\nBoom !")
# oneFile.write("\ndiiddidididdd\n67")
# print(oneFile.readable())
# print(oneFile.writable())
# oneFile.flush()
# oneFile.close()

# # read the file
# oneFileRead = open("abc.txt","r")
# print(oneFileRead.read())
# # print(oneFileRead.readlines())
# print(oneFileRead.readline())
# print(oneFileRead.readable())
# print(oneFileRead.name)
# print(oneFileRead.mode)
# print(oneFileRead.writable())
# print(oneFileRead.tell())
# print(oneFileRead.fileno())
# oneFileRead.close()
# # oneFileRead.close()

# fileFlush = open("abc.txt","w")
# fileFlush.flush()
# fileFlush.close()

# fileRead = open("abc.txt","r")
# print(fileRead.read())
# fileRead.close()

#r+ read and write

with open("abc.txt","r+") as readAndWrite:
    readAndWrite.write("Lorem Ipsum")
    readAndWrite.write("Hello World")
    # readAndWrite.seek(0)
    # data = readAndWrite.read() 

    # print(data)



with open("abc.txt","r+") as readAndWrite:
    # readAndWrite.seek(11)
    readAndWrite.write("Ipsum")
    readAndWrite.write("World")
    data = readAndWrite.read() 

    print(data)


#w+
with open("news.txt","w+") as readandWrite:
    readandWrite.write("Warner is the captain of KK !")
    # readandWrite.seek(0)
    readandWrite.write("Warner")
    # print(readandWrite.read())

with open("news.txt","w+") as readandWrite:
    # readandWrite.write("Warner is the captain of KK !")
    # readandWrite.seek(0)
    readandWrite.write("Warner")
    # print(readandWrite.read())


#a+
with open("woo.txt","a+") as readandAppend:
    readandAppend.write("Warner is the captain of KK !")
    # readandWrite.seek(0)
    readandAppend.write("Warner")
    # print(readandWrite.read())

with open("woo.txt","a+") as readandAppend:
    # readandWrite.write("Warner is the captain of KK !")
    readandAppend.write("Warner")
    readandAppend.seek(0)
    print(readandAppend.read())


#x
# with open("x.txt","x") as createUniqueFile:
#     createUniqueFile.write("lorem ipsum")
#     createUniqueFile.write("Karachi")


# with open("x.txt","x") as createUniqueFile:
#     createUniqueFile.write("\n ipsum")
    

#x+
# with open("xplus.txt","x+") as uniqueFileReadAndWrite:
#     uniqueFileReadAndWrite.write("I will be a billionaire")
#     uniqueFileReadAndWrite.seek(0)
#     print(uniqueFileReadAndWrite.read())


#b
with open("download__1_-removebg-preview (2).png","br") as binaryRead:
  petrolImg = binaryRead.read()

with open("copy.png","bw") as imgWrite:
   imgWrite.write(petrolImg)
