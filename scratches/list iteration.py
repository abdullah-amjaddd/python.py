w=[10,20,30,"Assalamulaikum"]
t=len(w)
print(t)
for a in range(t):
    print(w[a])#this will iterate the whole list because a will iterate the length from 1 to 3
print()
for a in w:
    print(a)#this will iterate the whole string
print()
#now we will print the list in reverse using for loop
s=[10,20,30,40,50]
k=len(s)
print(k)
for b in range(k-1,-1,-1):
    print(s[b])#the use of range is must in reversing string as well as list
#if we print only b it will only show index number not the values therefore
#we print the variable s as well as the variable which has the index number b
#such that s has the values of the index and b has index number
#output
#1st iteration--50 2nd --40 --3rd iteration30