# Tuples

ourTuple = (10,20,30,40,50)
print(ourTuple[1:2])
print(ourTuple*2)

print(len(ourTuple))

print(ourTuple.index(20))
a,b,c,d,e = ourTuple
print(a,b,c)

ourTuple2 = (10,20,30,40,50)
print(id(ourTuple2) , id(ourTuple))
a,b,c,d,e = ourTuple2
print(a,b,c,d,e)

#using * to capture multiple values
f,g,*h,i = ourTuple2
print(f)
print(g)
print(h)
print(i)