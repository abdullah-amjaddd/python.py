Position_Holders={'Umair':{'Marks':90,'Position':'First'},'Ali':{'Marks':86,'Position':'Second'},'Amir':{'Marks':85,'Position':'Third'}}
print(Position_Holders)#here is the nested dictionary concept where there is many dictionaries inside a single dictionary
#if we want to update the marks of a certain student then the logic will be given below
Position_Holders['Umair']['Marks']=93
print(Position_Holders)#the marks is now updated to 93
#another examples
courses={'Ai/Ml':{'fees':68000,'duration':'4months'},'Cloud Computing':{'fees':50000,'duration':'6months'}}
print(courses)
#we can also print the targeted dictionary
print(courses['Cloud Computing']['duration'])# by passing the dict name you want to see inside square bracket
#if we want the whole dict at once then we willl use for loop
for k,v in courses.items():#items is used to give the keys and values of the dictionary
    print(k,v)#this will give the ans in seperate rows of each dictionary\
    print(k,v['fees'],v['duration'])#this will give the output normally not in curly braces