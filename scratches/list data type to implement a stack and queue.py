#stack is a linear data structure that stores data in lifo or fif manner
#stores data in a sequential format
l=[]
while (True):
    c=int(input("""
    1 push element
    2 pop element(deletes the last element
    3 peek(display) last element 
    4 display the whole list
    5 Exit
    """))
    if c==1:
        n=input("Enter the value")
        l.append(n)
        print(l)
    elif c==2:
      if len(l)==0:#because the list is empty so it will result in an empty stack message
    #on the output console
          print("Empty stack")
      else:
          p=l.pop()#pop function will delete the last element if it is available in the index
          print(p)
          print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty stack")
        else:
            print("Last stack Value",l[-1])
    elif c==4:
        print("Display all the stack values",l[-1])
    elif c==5:
        break#exit from the while loop
    else:
        print("Invalid operation!")#give a display error message if you type out of range choices
#for example 7 



