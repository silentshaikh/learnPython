# Tokenization (Lexical Analysis)

# import tokenize
# from io import BytesIO

# code = b'print("Hello, World!")'
# for token in tokenize.tokenize(BytesIO(code).readline):
#     print(token)


# Parsing & AST (Abstract Syntax Tree)
# import ast
# tree = ast.parse('print("Hello, World!")')
# print(ast.dump(tree,indent=4))

# Bytecode Generation

# import dis
# dis.dis('print("Hello, World!")')

# Memory Management
# import sys

# a = [1, 2,3]
# b = a  # Both 'a' and 'b' point to the same list

# print(sys.getrefcount(a))  # Shows reference count

# Bytes
ab = b"Hello World"
# print(type(ab),ab)

#Memory View
mem_view: memoryview = memoryview(b"Operation Badar")
print(mem_view)
num1 = 100
num2 = 100
print(id(num1) == id(num2))
# print(id(100) == id(100))
str1 = "hello"
str2 = "hello"
print(id(str1) == id(str2))
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5]
arr3 = arr1
print(id(arr1) == id(arr2))
print(id(arr1) is id(arr2))
print(id(arr3) is id(arr1))
print(arr3 is arr1)

#Memory space sharing
# a = 100
# b= 100
a= 1000
b=1000
print(id(a),id(b))
print(id(a) == id(b))
print(a is b)
print(id(a) is id(b))


# Bitwise operator

p = ~5
print(p)

# Identity Operators
print("Identity Operators")
a = 5
b = 5
print(a == b)

i = ["Apple","Banana","Orange"]
j = i
k = ["Apple","Banana","Orange"]
print(i == j)
print(i is k)
print(i is not k)

# Delete a variable
gone = "Gone"
print(gone)
del gone
print(gone)