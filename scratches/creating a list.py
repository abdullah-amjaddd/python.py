#list is just like an array
l=[1,2,3,4,5]
print(l[1])
#list is a mutable data type can be change edit or deleted
#its index number starts from 0
#we can also assign a list inside another list
s=[6,7,8,[9,10,11]]
print(s[3][1])#the range of the inside list is 3 and the index we want to print of
#the inside list is written after list index
print(type(l))
#now lets create a mix list
b=[1,2,3,"Hello",[4,5,6]]
print(b[3])
print(b[4][2])
#slicing a list
print(b[0:5])#the start point is 0 and the condition become false at index 4
print(b[0:])#if we leave the ending point blank then it will run till the last index is printed
w=[1,2,3,4,5,6]
print(w[0::2])#this will print the odd numbers in the list by incrementing 2
#if we want to print in reverse then below will be correct way
print(w[-1::-2])