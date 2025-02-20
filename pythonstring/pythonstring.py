#string
name = "Lorem Ipsum"

#multiline string
para = """lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development to fill empty spaces in a layout that does not yet have contenT."""

print(name)
print(para)
print(para[4])

# String Slicing
slicePara =para[0:10]
print('Slice String : ',slicePara)

#Format String
intro = f"My name is Sam and my age is {20}"
print(intro)

#Escape Characters
# '/
one = "Hello, My name is \"Abdul Moiz\" 12345"
print(one)
two = 'abc123'
deci = "45"
#string Method
print(para.capitalize())  # convert first letter in capital
print(para.upper()) # convert all letter in capital
print(para.lower()) # convert all letter in small
print(para.title()) # convert first letter of each word in capital
print(para.casefold())  # convert all letter in small
print(para.count('l')) # return the count of a specific word

paraEnds = para.endswith("t.") # True or False if a specific word end with the specific value or not
print(paraEnds)
paraStart = para.startswith('l') # True or False if a specific word start with the specific value or not
print(paraStart)
paraFind = para.find('t') # find the string of a spefic value and then return the position of string
print(paraFind)
paraIndex = para.index('t') # search the string of a spefic value and then return the position of string
print(paraIndex)
twoAlphaNum = two.isalnum() # return true if string is alphanumeric
print(twoAlphaNum)
paraAlpha = name.isalpha() # return true if string is alphabetic
print(paraAlpha)
numDecim = deci.isdecimal() # return true if string is decimal
print(numDecim)
numDigits = "\u00B2".isdigit()
print(numDigits)
print(two.islower()) # return true if string is lowercase
numNumeric = "4567".isnumeric() # return true if string is numeric 5,6,7
print(numNumeric)
print(name.isupper()) # return true if string is uppercase
print(name.istitle()) # return true if string is titlecase
arr = ["A","B","C"]
joinStr = "#".join(arr)
print(joinStr)
stripStr = "   Hello    ".strip() # remove whitespace from left and right
print(stripStr)
leftStrip = "   Hello    ".lstrip() # remove whitespace from left 
print(leftStrip)
rightStrip = "   Hello             ".rstrip() # remove whitespace from right
print(rightStrip)
lJustStr = "His name is ".ljust(20) # return a left justified version of string
print(lJustStr,"Harry")
rJustStr = "His name is ".rjust(20) # return a right justified version of string
print(rJustStr,"Harry")
splitStr = "helloworld hello".split() # Splits the string at the specified separator, and returns a list
print(splitStr)
splitLineStr = "hello\nworld hello".splitlines() # Splits the string at line breaks and returns a list
print(splitLineStr)
swapStr = "Hello world WORLD".swapcase() # Swaps cases, lower case becomes upper case and vice versa
print(swapStr)
centerStr = "Apple".center(50) # return the banana with taking up the space of character on left and right , space like 20 ,30 etc
print(centerStr)
encodeStr = "Hurråh".encode() # return the encode version of string
print(encodeStr)
expandTabStr = "h\te\tl\tl\to".expandtabs(1)
print(expandTabStr)
formatStr = "Your Items price is ${price:.2f}".format(price=430)
print(formatStr)
fomatMapStr = "Your Items price is ${price:.2f}".format_map({"price":99})
print(fomatMapStr)
spaceStr = "   ".isspace() # return true string has only space
print(spaceStr)
replaceStr = "hello world".replace("h","y")
print(replaceStr)
translateStr = "Hello, Sam".translate({83:80}) 
print(translateStr)
identfierStr = "Hello".isidentifier() # return true if a string is a valid identifier
print(identfierStr)
printableStr = "hello, what are you \ doing".isprintable() # return true if string is printable
print(printableStr)
partitionStr = "You are liking pineapple many times".partition('many') # do partition with a specific word of string and then return the partition in tuple
print(partitionStr)
rPartitonStr = "You are liking pineapple many times liking".rpartition("liking") # do partition with a last word of string and then return the partition in tuple
print(rPartitonStr)