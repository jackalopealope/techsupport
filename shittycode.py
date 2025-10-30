#!/usr/bin/python3

#Define security code variables for use in checksum

#Values
global I
global II
global III
global IV
global V
global VI
global VII
global VIII
global IX
global X
#Query Strings
q0="What is the first letter of the city that your school is located in?\n"
q1="What grades are at this school? (e.g. for 3rd, 4th, 5th: 345)"
q2=""
q3=""
q4=""
q5=""
q6=""
q7=""
q8=""
q9=""



#Security Questions Code
def checklen(input,length):
    if len(input) == length: #Check if length is correct
        print("\nYou said:\n",input)
    else:
        #Exit Without Generating checksum
        print("Bad Input")
        input("\nPress enter key to exit")
        exit()
#Capitalize string to ensure proper checksum generation 
I = input(q0).capitalize()
#Ensure length of string is just one
checklen(I,1)
#Ensure variable is string
if isinstance(I,str) != True:
    print("Bad Input")
    input("\nPress enter key to exit")
    exit()

II = input(q1)
#Ensure Length is correct
checklen(II,3)
#Convert II to a integer for checksum generation
II = str(II)
print(str(I,II))





    


    
