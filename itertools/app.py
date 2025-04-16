import itertools

# for num in itertools.count(5,1):
#     if num > 25:
#         break
#     print(num)


# names = ['Alice', 'Bob', 'Charlie']
# for index,name in enumerate(itertools.cycle(names)):
#     if index>19:
#         break
#     print(index,name)


# print(itertools.repeat("Hello"))
# for value in itertools.repeat("Hello",10):
#     print(value)

# print(itertools.permutations("hello"))
# for strs in itertools.permutations("hello"):
    # print(strs)

# print(itertools.combinations("hello",2))
# for strs in itertools.combinations("hello",5):
#     print(strs)

# for strs in itertools.combinations_with_replacement("hello",5):
#     print(strs)

# for item in itertools.product(["red","green","blue"],["T-Shirt","Shirt"]):
#     print(item)


items = ["Apple", "Banana", "Orange", "Carrot"]

# Define a function that classifies items
def categorize(item):
    return "Fruits" if item in ["Apple", "Banana", "Orange"] else "Veges"

# Sort the list so groupby() works correctly
items.sort(key=categorize)

# Apply groupby with the categorize function
for key, group in itertools.groupby(items, key=categorize):
    print(f"{key}: {list(group)}")