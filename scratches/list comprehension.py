l=[]
for a in range(1,101):
    l.append(a)#append function is used to add a single item to certain collection types
print(l)
n=[h for h in range(1,101) if h%2==0]#we can also involve conditional statements
#using if statements in list comprehension
print(n)#the logic is same in both the cases
#it makes the program compact because the output will use single or less line than
#normal printing of a number through iteration for example if we use norml iteration it will
# #100 lines to print the output but with use of list comprehension it will take only 3 to 4 lines
# making a list thats why it is faster and compact
#below example is use of string in list comprehension
y="Harry"
f=[q for q in y]
print(f)#this will print string in a list
