s="Hello World"
#method of string reverse
# s=s[-1::-1]
t=len(s)
print(t)#here len is a builtin func used to calculate length of the string
for a in range(t):
    # print(a) this will iterate the whole length from 0 to 20
    print(s[a])#this will iterate the characters in the string
    #for example s[0]=H s[1]=e s[2]=l
print("")
#another method of reversing string using for loop
for a in range(t-1,-1,-1):#the loop starts from index 20 till the condition is 0
    #index and for that it decrements -1 in each iteration
    print(s[a])