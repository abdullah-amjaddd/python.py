a=10
print(a,type(a))
a=10.5
print(a,type(a))
a=20+11j
print(a,type(a)) #type is a builtin function determine the type of variable
b="my name is abdullah amjad"
print(b,type(b))
s='''I am an 18 year old boy
from karachi pakistan 
pursuing a degree in
bscs
'''
print(s,type(s)) #triple quotational string
l=[20,"Abdullah",3.5,40]#list data type can be changed because mutable
print(l,type(l))
l[3]=30#the index number starts from 0
print(l,type(l))#the value is changed from 40 to 30
#tuple is same as list with minor differences but faster than list
#it is immutable and are defined with parenthesis
t=(10,4.7,"Abdullah Amjad")
#print(t,type(t))
#t[2]="Umair "
#print(t,type(t)) tuple does not support updation thats why its faster than list
d={'course_name':'python',#dictionary is immutable data type which is
'course_duration':'6 months'}#unordered collection of key value pairs
#it can be updated by the key of the value you want to change
print(d,type(d))
print(d['course_duration'])
#set is an unordered collection of unique element.all the element in set must be uniq
#if same element occurs it automatically removes it
s={10,20,30,40,40,50}
print(s,type(s))
#the output is unordered in sets
