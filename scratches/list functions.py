#functions for deleting element from list del(),remove(),pop(),clear()
s=[10,20,30,40,50]
del s[2]#delete function deletes an element from list but doesnt return the elemeent
print(s)
w=[90,80,70,60]
print(w.pop(1))
print(w)#only difference btw pop and delete is pop returns the deleted element by printing it
p=[30,68,79,9,89]
p.remove(79)#remove is a builtin function and you pass the direct value not the
#index in parameter of remove functions
print(p)
#clear is builtin function use to clear the whole list doesnt work on single element
o=[20,30,40,50,60]
o.clear()
print(o)

