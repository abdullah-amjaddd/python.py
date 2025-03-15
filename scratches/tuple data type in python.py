#tuple is an immutable data type and is ordered data type
#values are assigned in rounded brackets in tuple() elements are seperated by comas
#as it is ordered so it works on indexing
#imp thing to note a single element inside round bracket is nut tuple tupple must have
#more than single elements example given below
t="Abdullah amjad"
print(type(t))#this will give output as string because there is only one element
#to iterate a tuple we use for loop
s=(10,20,30,40)
# w=len(s)
# for a in range(w):
#     # print(a)#this will give index position only
#     print(s[a])#this will give the value at each index position
#another method of iterating the whole tuple
for a in s:
    print(a)#this will iterate the whole tuple
print()
#lets talk about tuple functions
#min()function is used to return the minimum element while max returns maximum
p=(10,20,30,10,10,90)
q1=min(p)
print(q1)
q2=max(p)
print(q2)
#count function returns the number of count of each element
p2=p.count(10)
print(p2)#gives output as 3 because is 10 is present 3 times in tuple
#index gives the index number of the value
p3=p.index(30)
print(p3)#the index number of 30 is 2
#sum()function only works on float and integers not string it returns the sum of the tuple
b=sum(p,30)#here 30 is the default value of sum beefore interpreting so sum will be 200
print(b)#we can also pass two arguments in sum function