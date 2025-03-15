#use of zip function
l=[10,20,30,40,50]
t=len(l)
l1=[100,200,300,400,500]
for a,b in zip(l,l1):#zip function is used to iterate two lists at the same time
#as we have two lists so we pass two paraameters a,b and print a,b while range is l and l1
#and the function is zip
    print(a,"x",10,"=",b)
print()
#if the no of elements are not same then zip will not print the exceeded element
#for ex if one list has 4 elements and list 2 has five elements then the fifth
#element will be ignored by the interpreter
l3=[10,20,30,40]
l4=[50,60,70,80,90]
for c,d in zip(l3,l4):
    print(c,d)#in the output 90 is not printed
print()
#another formula to iterate two lists without using zip function
for h in range(t):
    print(l[h],l1[h])#this will iterate both lists without zip
print()