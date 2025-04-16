from string import Template
import sys
# # String 

# # Escape Sequence
# print('Hello \'World\'')
# print("Hello \"World\"")
# print("Hello \\World")
# print("Hello \nWorld")
# print("Hello \tWorld")
# print("Hello \rWorld")
# print("Hello \bWorld")
# print("Hello \fWorld")
# print("Hello \vWorld")
# print(r"C:\Users\Admin")  # raw string
# print("\000")
# # print("\xhh")

# # Unicode Character
# print("\u2764")
# print("\U0001F600")
# # The chr() function converts a Unicode code point into a character:
# print(chr(10084))

# # Slicing in String
# ourStr='Hello, World'
# print(ourStr[:])
# print(ourStr[2:8])
# print(ourStr[3:])
# print(ourStr[:3])
# print(ourStr[0:10:2])
# # print(ourStr[0:10:1]) it will not work
# print(ourStr[1:10:-2])
# print(ourStr[::-1]) # reverse the string

# text1 = "Python"
# print(text1[2:2])
# print(text1[100:])
# print(text1[:5000])
# print(text1[-6:])
# print(text1[::-1][::-1])
# print(text1[-1:-len(text1)-1:-1][::-1])
# print(text1[-1:-len(text1)-1:-1])


# String Methods
myStr = "Hello, World"

# Case Conversion

# strToUpper = myStr.upper()
# print(strToUpper)
# strToLower = myStr.lower()
# print(strToLower)
# strToCapitalize = myStr.capitalize()
# print(strToCapitalize)
# strToTitle = myStr.title()
# print(strToTitle)
# strToSwap = myStr.swapcase()
# print(strToSwap)

# String Checking Methods (Boolean)
strIsAlpha = myStr.isalpha()
print(strIsAlpha)
digits = "1.4".isdigit()
print(digits)
strIsAlnum = "hello123".isalnum()
print(strIsAlnum)
strIsSpace = " ".isspace()
print(strIsSpace)
strisLower = "hello12@".islower()
print(strisLower)
strisUpper = 'HELLO12@'.isupper()
print(strisUpper)
strisTitle = 'Hello World12@ g'.istitle()
print(strisTitle)
strIsDecimal  = "12345.6".isdecimal()
print(strIsDecimal)
strIsPrintable = "\u2464".isprintable()
print(strIsPrintable)
strIsIdentifier = "Hello_123.6".isidentifier()
print(strIsIdentifier)
strIsAscii = "Hello12.3\n$ ".isascii()
print(strIsAscii)

text = "Hello\nWorld\rPython\r\nCoding"

print(text.splitlines(True))

#String Formation
formtStr = "Hello World"
print("Format :",formtStr.center(20,"-"))

#startswith
print(formtStr.lower().startswith("Hello".lower(),0))
print(formtStr.lower().startswith("World".lower(),6))

#encode
print(formtStr.encode())
print(formtStr.encode("utf-16"))
print(formtStr.encode("latin-1"))
# print(formtStr.encode("lati1",errors="Wrong encode"))

encodeStr = formtStr.encode("utf-16")
print(encodeStr)
decodeStr = encodeStr.decode("utf-16",errors='Invalid encode')
print(decodeStr)

#String Formating
strFormt = 'Hello %s World !'% formtStr
print(strFormt)
strFormt2 = "Roll No %d"% -24
print(strFormt2)
strFormt3 = "Percentage : %f"%34.56
print(strFormt3)
strFormt4 = "Name : %coiz"%"M"
print(strFormt4)
strFormt5 = "%.3f" % 34.4555756867
print(strFormt5)

# Template Strings (Useful for Security)
myName = "Abdul Moiz"
templ = Template("My Name is $myName")
print(templ.substitute(myName=myName))

#Does not matter
myName = "Abdul Moiz"
print("My Name is {name}".format(name=myName))
print("My Name is {0} and My age is {1}".format(myName,20))

#Pool of String Literals in Python
pol1 = "hello worl@d!"
# pol2 = "hello worl@d!"
pol2 = "".join(['hello','worl@d!'])
print( pol1 is pol2)

pol3 = 'aaaaaaaaaaaaaaaaaaaaa'
pol4 = 'aaaaaaaaaaaaaaaaaaaaa'
print(id(pol3) , id(pol4))

# To FOrce Interning
pol5 = sys.intern('aaaaaaaaaaaaaaaaaaaaaaa!')
pol6 = sys.intern('aaaaaaaaaaaaaaaaaaaaaaa!')
print('Force INterning : ',pol5 is pol6)