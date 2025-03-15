l=[]
while (True):
    c=int(input("""
    1 push element
    2 pop element
    3 front element
    4 last element
    5 display queue
    6 Exit
    """))
    if c==1:
        n=input("Enter the value")
        l.append(n)#append the value user entered in the list
        print(l)
    elif c==2:
      if len(l)==0:#returns empty queue if no value is assigned in the queue known as enqueue
          print("Empty queue")
      else:
          del l[0]#else delete the first element of the list this process is known as dequeue

          print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("first queue value",l[0])#print the first queue value also known as front value
    elif c==4:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("last queue value",l[-1])#print the last queue value known as rear
        if len(l)==0:
         print("Display  queue ",l[1])
    elif c==5:
            print("Display all values in the queue",l)#display all values in the queue
    elif c==6:
        break
    else:
        print("Invalid operation!")
