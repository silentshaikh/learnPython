# def add(a,b,/,c):
#     print(a+b+c)

# add(1,2,3)

# def upPack(*args):
#     print(*args)

# upPack(*[1,2,3,4,5,6,7])
# upPack(*(1,2,3,4,5,6,7))
# upPack(*{1,2,3,4,5,6,7})
# upPack(*{"name":"Sam"})


# def kwrg(**kwargs):
#     for key,item in kwargs.items():
#         print(key,item)


# kwrg(one=1,two=2)
# kwrg(**{"one":1,"two":2})
# # def keywordOnly(th,*,):
# def keywordOnly(name,*,age):
#     print(name,age)

# keywordOnly('Sam',age=20)
# keywordOnly('Sam',20)


# Generator Function

def infiniteNum():
    num =1
    while True:
        yield num
        num+=1

print(next(infiniteNum()))
print(next(infiniteNum()))
print(next(infiniteNum()))

infiNum = infiniteNum()
print(infiNum)
print(next(infiNum))
print(next(infiNum))
print(next(infiNum))
print(next(infiNum))

def counter(start, end):
    while start <= end:
        yield start
        start += 1

gen = counter(1, 3)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Raises StopIteration
