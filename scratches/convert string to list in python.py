# j=input("Enter a value")
# l=j.split()#The split() method splits a string into a list.space is mandatory for splitting
# #if we didnt give space after each word it prints the entire sentence or string as one word
# print(l)
# e=[]
l=[]
for a in range(1,4):
    n=input("Enter the value"+str(a)+":-")
    print(n)#the program takes user input three time and store it in variable n
    l.append(n)#the append function append all the input into l list such that the string
#appears as list
print(l)