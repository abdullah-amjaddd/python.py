d={'Name':'Abdullah','Age':'18','HomeTown':'Karachi'}
# n=d.get("Name")
# print(n)#get function gets the value through the unique key of that value
# #key function is used to get all the key values from dictionary d but use of for loop is must
# for a in d.keys():
#     print(a)
# print()
# #values function is used to get all the values from the dictionary
# for b in d.values():
#     print(b)#this will print all the values of the keys
# print()
# #the item function is used to get both keys and values
# for c,d in d.items():
#     print(c,d)#prints both keys and values
# print()
# #now we will talk about other function
# #del() and pop() are use to delete and remove the key or values from dictionary
# #for example
# del d['Age']#delete the key named As Age as well as value 18
# print(d)
#we can also use pop to remove keys and values from dictionary
print(d.pop('Age'))#also pops return which thing he has deleted
print(d)#pops the key named as Age as wellas value 18
#now we will take about dict()
l=dict(Name='Umar',Age='20')
print(l)#dict is used to create a dictionary
#update() is used to update the values of a certin key in dictionary
t={'Name':'Abdullah Amjad','Age':'18'}
#now if i want to update my age i will use update()
t.update({'Age':20})#thus the age is updated to 20 in the dictionary
print(t)
#clear() is used to clear all the data inside the dictionary
t.clear()
print(t)#this will give a blank dictionary
#process of inserting an new element in the dictionary
w={'Name':'aslam','Age':'21'}
w['Hometown']='Lahore'#here hometown is key and lahore is python
print(w)