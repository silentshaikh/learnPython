# Dictionary in Python

dict1 = {
    'name':'Sam',
    'country':'USA'
}

# del dict1['name']
print(dict1)

#perform operation using membership operators
if 'name' in dict1:
    print("yes")
else:
    print('no')

if 'name' not in dict1:
    print('yes')
else:
    print('no')


# Dictionaries Methods

# get()
print(dict1.get("name"))
print(dict1.get('city','New York')) # set a default if key doesn't exist in dictionary

# keys()
changesReflects = dict1.keys()
dict1['city'] = "new york"

print(type(changesReflects),changesReflects)

# values()
changesReflets = dict1.values()
dict1['city'] = 'chicago'
print(type(changesReflets),changesReflets)

#items()
changeReflect = dict1.items()
dict1['course'] = 'AI'
print(type(changeReflect),changeReflect)

#update()

dict1.update({'father':"SMA"})
dict1.update(sports='Cricket')
dict1.update([('name','lorem'),('second','ipsum')])
print(dict1)

#pop()
# print(type(dict1.pop('second')))
# print(dict1.pop('sec','not found'))
# print(dict1)

#popitem()
# print(dict1.popitem())
# print(dict1)

#clear()
dict1.clear()
print(dict1)

#copy
dict2 = {
    "sam":[334523443],
    "tom":5354564565756,
    'group':{
        'one':'wedweew',
        'two':'werrferg'
    }
}

copyDict2 = dict2.copy()
copyDict2['tom'] = 8888888888888
copyDict2['sam'][0] = 35346456575667867
print('Copy',copyDict2)
print("Original",dict2)


#fromkeys()

newDict = dict.fromkeys([1,2,3],['Sam','Tom',"Jerry"])
newDict[1].append("xyz") 
print(newDict)
print(copyDict2)
copyDict2 = copyDict2.fromkeys('lorem',[])
copyDict2['l'] = ['hello']
print(copyDict2)

#setdefault
myDict = {
    'name':'Sam',
    'country': "USA"
}
print(myDict.setdefault('name'))