#sets is a unordered data type and doesnt work on indexing it is defined in curly braces
#just like the dictionary data type but the difference is that sets doesnt work on key value pair
s={10,20,30,40,50,10}
print(type(s))
print(s)#the answer on output screen is unordered not in sequence for ex 50 20 40 10 30
#set is a unique data type if the element is repeating it will use it once for example
print(s)#the second 10 is ignored by the interpreter
#to iterate set we use for loop
for a in s:
    print(a)#this will give the all elements in sets
print()
#now we will talk about functions used in sets data type
#now we will talk about set() function
#set() is used to convert a list or tuple to sets data type
l=[10,30,90,80]
s=set(l)#convert to sets data type from list
print(s)#the output will be random no sequence in sets
#you can convert a tuple to
l1=(10,20,30,40)
s1=set(l1)#convert tuple to sets
print(s1)
#remove() function is used to remove an element from the set randomly
o={10,29,30,40,50}
o.remove(29)#removes 29
print(o)
#pop() function is similar to remove and discard()
o1={10,90,80,70}
o1.pop()#no arguments can be given deletes or removes an element randomly
print(o1)
#discard() function is used to discard an element from sets
o2={10,20,30,40,50}
o2.discard(10)#discard 10 from the sets
print(o2)
#only difference between pop,remove,duscard is we cant take arguments in pop while we can\
#in remove and discard
#now add function is used to add a new element in the sets
w2={10,20,30,40}
w2.add(300)
print(w2)#300 is added
#now we will talk about update() as set is inmutable data type
#it is used to update list to sets data type
w3={10,20,30,40,50}#sets
l5=[70,30,40,90]#lists
w3.update(l5)
print(w3)#update the lists element into sets data type
#we can do it for tuple also
w4={10,20,30,40,50}#sets
f=(60,70,80,90)#tuple
w4.update(f)
print(w4)#update the tuple elements into sets data type
#now we will talk about clear() function
y={10,20,30,40,50}
y.clear()
print(y)#gives a blank list clearing all the element 