#!/usr/bin/python3
import string

#Security Questions Code
def checklen(input,length):
    if len(input) == length: #Check if length is correct
        print("\nYou said:\n",input)
    else:
        #Exit Without Generating checksum
        print("Bad Input")
        input("\nPress enter key to exit . . . ")
        exit()

#main array for checksum
strqcksum=[]
#Query Strings
strqcksum[0] =input("What is the first letter of the city that your school is located in? ").capitalize()
strqcksum[1] =input("What grades are at this school? (e.g. for 3rd, 4th, 5th: 345) ")
strqcksum[2] =input("Who teaches history hijinks [Put last name only. For Ms. Example you would just put 'example'] ").capitalize()



def checksumgen():
    #Capitalize string to ensure proper checksum generation 
    I = strqcksum[0]
    #Ensure length of string is just one
    checklen(I,1)
    #Ensure variable is string
    if isinstance(I,str) != True:
        print("Bad Input or Incorrect Answer")
        input("\nPress enter key to exit . . . ")
        exit()

    II = strqcksum[1]
    III = strqcksum[2]
    #Ensure Length is correct
    checklen(II,3)
    checklen(III,6)
    #Convert Variables to integers for checksum generation
    #Convert I to its alphabetical index plus one so that it wont set the full checksum to 0 when multiplies
    I = string.ascii_uppercase.index(I)+1
    II = int(II)+1
    III = string.ascii_uppercase.index(III)+1
    #Development code only
    print((I,II,III))


checksumgen()
input("\nPress enter key to exit . . . ")

    


    
