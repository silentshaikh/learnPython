with open("lorem.txt","w") as fileone:
    print(fileone.fileno())
    print(fileone.seekable())
    fileone.write("Lorem Ipsum")
    fileone.write("45")
    fileone.write("jnejnrifneuinfvdfknvjwenruinrufnvjnfjvndfnjnrtgurjfnvkdnfvknfnrgijgujutngntgnjnvghbhbvhgbhg")

with open("lorem.txt","r") as fileTwo:
    print(fileTwo.fileno())
    print(fileTwo.seekable())
    fileTwo.seek(5)
    print(len(fileTwo.read()))
    print(fileTwo.tell())


# with br
with open("binary.txt","wb") as binaryWrite:
    
    print(binaryWrite.seekable())
    binaryWrite.write(b"Lorem Ipsum")
    binaryWrite.write(b"45")
    binaryWrite.seek(5)
    binaryWrite.write(b"jnejnrifneuinfvdfknvjwenruinrufnvjnfjvndfnjnrtgurjfnvkdnfvknfnr")

with open("binary.txt","rb") as binaryRead:
    print(binaryRead.seekable())
    binaryRead.seek(-3,2)
    print(binaryRead.read())
    print(binaryRead.tell())

with open("appenddata.txt","a+") as appendData:
    print(appendData.seekable())
    # appendData.write("lorem45")
    appendData.write("lorem45")
    appendData.seek(5)
    appendData.write("ipsum")
    print(appendData.tell())
    appendData.seek(0)
    print(appendData.read())

with open("truncatedata.txt","w+") as truncOne:
    # truncOne.write("123456789012345678901234567890")
    truncOne.truncate(10)


with open("truncatedata2.txt","w") as truncTwo:
    truncTwo.write('abcdefghijklmnopqrstuvwxyz')
    # truncTwo.truncate(15)

with open("truncatedata3.txt","bw+") as truncThree:
    truncThree.write(b"abcdefghijklmnopqrstuvwxyz")
    # truncThree.truncate(15)

with open("truncatedata3.txt","r+") as truncFour:
    # truncFour.write("abcdefghijklmnopqrstuvwxyz")
    truncFour.truncate(20)

with open("truncatedata4.txt","a") as truncFive:
    # truncFive.write("abcdefghijklmnopqrstuvwxyz")
    # truncFive.seek(0)
    truncFive.truncate(20)
    print(truncFive.fileno())

with open("truncatedata2.txt","a+") as truncSix:
    # truncSix.write("abcdefghijklmnopqrstuvwxyz")
    # truncSix.seek(0)
    print(truncSix.fileno())
    truncSix.truncate(15)

fileThree = open('flush.txt','w')
fileThree.write("abcdefghijklmnopqrstuvwxy")
# fileThree.flush()
print(fileThree.fileno())
fileThree.close()
fileFour = open("flush.txt","r")
# fileFour.write("erfbebbfbreufiehffjjv")
# fileFour.flush()
print(fileFour.fileno())