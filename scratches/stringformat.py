txt1="Welcome {fname} Ws {lname}".format(fname="to",lname="Cubetech")
print(txt1)
#the placeholder is placed inside the curly bracket and get the value through the parameters passed
#inside the fname or lname variable and we type the variable inside the curly bracket to do formatting
txt2="Welcome {0} ws {1}".format("to","CubeTech")
print(txt2)#this process is known as numbering index the format function through the index paced in the curly bracker
#identifies what to print of the parameters passed in the function through their index
#empty placeholders below
txt3="Welcome to {} {}".format("Wscube","Tech")
print(txt3)
#the three ways are used for formatting
txt1="Welcome {fname:5} Ws {lname}".format(fname="to",lname="Cubetech")
print(txt1)#you can also do spacing by just putting colon and the range of space by putting a number
txt1="Welcome {fname:^5} Ws {lname}".format(fname="to",lname="Cubetech")
print(txt1)#the ^ symbol will print the string between and provide spaces left and right only
txt1="Welcome {fname:<5} Ws {lname}".format(fname="to",lname="Cubetech")
print(txt1)#< symbol gives spaces to the right side after the string
txt1="Welcome {fname:>5} Ws {lname}".format(fname="to",lname="Cubetech")
print(txt1)#the space will go to left side before the string
#for example
#if the spacing is 10 and the symbol is^ then ----10---- this will be the output
#if > then --------10 and < then 10--------