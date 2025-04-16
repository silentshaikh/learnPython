ourSet = {34,2,1,5,6,False,7,0,False}
print(ourSet)
# ourSet[0] = 56   #we can't access sets with index

# In Set's, we can't store mutable data like list and dictionaries
newSet = {2,3,("apple","banana"),4,"hello",True} 
print(newSet)

# Sets Methods

#add()
newSet.add(5)
print("add()",newSet)

#remove
newSet.remove(5)
print("remove()",newSet)

#pop()
print(newSet.pop())
print("pop()",newSet)

#clear()
sets = set()
sets.clear()
print('clear()',sets)

#update()

newSet.update('67')
newSet.update({6,7})
newSet.update([8,9,"8"])
newSet.update({11:'eleven',12:'twelve'},[13])
print("update()",newSet)


#union()

anotherSet = ourSet.union(newSet,"world",[15,16],{17},(18,19),{20:'twenty',21:'twenty one'})
print("union()",anotherSet)

#intersection()
intersecSet = newSet.intersection([1,2,3,4,5,6,7,8,9,"8"],{8,"8"},"8")
print("intersection()",intersecSet)


#intersection_update()
twoSet = {1,2,3,4,5,6,7}
twoSet.intersection_update({7},[7],{7})
print("intersection_update()",twoSet)

#difference()
theSet = {1,2,3,4,5,6,7,8}
set2 = {3, 4, 7, 8}
set3 = {5, 6, 9, 10}
diffSet = set3.difference(set2,theSet)
print("difference()",diffSet)

# difference_update()
theSet.difference_update(set2,set3)
print("difference_update()",theSet)

#symmetric_difference()

set4 = {1,2,3,4,5,6,7,8}
set5 = {5,6,7,8,9,10,11,12}
set4_5 = set4.symmetric_difference(set5)
print("symmetric_difference()",set4_5)

#symmetric_difference_update()
set4.symmetric_difference_update(set5)
print("symmetric_difference_update()",set4)

#issubset()

set6 = {1,2,3,10}
set7 = {1,2,3,4,5,6,7,8,9}
print("issubset()",set6.issubset({1:'onw',2:'two',3:'three',10:'ten'}))

#issuperset()

set8 = {1,2,3,4,5,6,7,8,9,10}
set9 = {1,2,3,4}
print("issuperset()",set8.issuperset(set9))

#isdisjoint()
set11 = {1,2,3,4}
set10 = {5,6,7,8}
print("isdisjoint()",set11.isdisjoint(set10))

#copy()
set12 = {1,2,3,4,5,6,"hello",(7,8)}
setCopy = set12.copy()
setRefrence = set12
print("copy()",setCopy)
set12.add(9)
print(setRefrence)
print("copy()",setCopy)