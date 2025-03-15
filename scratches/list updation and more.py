#as we know that list is a mutable data type so we can update or change its assigned
#element below program is an example
l=[10,20,30,40,90,68,58]
l[4]=50#list 4 index position is changed from 90 to 50 do it will be printed 50
print(l)
#below are the functions to update list
w=[10,20,30,40,50]
w.insert(0,15)
#here in insert function 0 is the index and 15 is the value we want to insert
#at that position
print(w)
e=[10,20,30,40]
e.append(60)#append function is used to add a single element at the endth position of
#the list for example 60 is appeared at the last position of the list
print(e)
#another example
k=[20,30,40]
n=[20,30,40]
k.append(n)
print(k)#print the list of n at last of the k list
#extend function below
u=[20,30,90,80]
m=[100,110]
u.extend(m)
print(u)#the only difference is the appended values of m are not in list
#you can check it by running the program
