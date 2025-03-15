#find function
a="AbdullahAmjad123"
print(a.find('b'))#the find function will find the index num of character in the assign string
print(a.find('A',4))#the 4 is the starting point of th efind function to find A in the string
#therefore we can also set the default index starting point in find function
#whats the case if the character you want to find is not available in the string
print(a.find('z'))#if char is not available in the string then result will be -1
#find and index are the same type of function that returns the index number of the string
b="I am going home"
print(b.index("g",6))#same functionality as of find function
#lets talk about is alpha() function
print(b.isalpha())#as there are spaces so it will print false
print(a.isalnum())#checks if string has both alphabets and numbers
w=("12345")
print(w.isdigit())#returns true if string is a digit