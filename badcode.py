#!/usr/bin/python3
import string

# Query Strings
q0 = "What is the first letter of the city that your school is located in?\n"
q1 = "What grades are at this school? (e.g. for 3rd, 4th, 5th: 345)\n"
q2 = "Who teaches history hijinks [Put last name only. For Ms. Example you would just put 'example']\n"

# Security Questions Code
def checklen(input_str, length):
    if len(input_str) == length:
        print("\nYou said:\n", input_str)
    else:
        print("Bad Input")
        input("\nPress enter key to exit")
        exit()

# Get inputs
I = input(q0).capitalize()
checklen(I, 1)

II = input(q1)
checklen(II, 3)

III = input(q2).upper()
checklen(III, 6)

# Convert variables for checksum generation
# Convert I to its alphabetical index plus one
# using string.ascii_uppercase.index() on a single character
I_checksum = string.ascii_uppercase.index(I) + 1

# Convert II to an integer and add one
II_checksum = int(II) + 1

# Convert III (a string of letters) to the sum of its alphabetical indexes plus one
# using a list comprehension and sum()
III_checksum = sum(ord(char) - ord('A') + 1 for char in III)

checksum = hex((int(I_checksum)**int(II_checksum)+int(III_checksum)**17))

if checksum != "0x11646cc7d1146e5e3047340433a1ccf871e03f7da9406e710b00af900cca2729a3cd8795e4218c66cbe31fbc5acee7f6ade38c061724c5e6d04bef144b08506bb6ddd4dc063eb6b6e5ba6a4163fce499b81f127947446faf52f12891130aef0c8fa3feabb47831871fff11437c3b057cd604c935feb0036e8e68902f2e393ea35488ff49ca04a302600ae60fc4924cb92ff31d6a6931f9904cc11c7419000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001259ef91b18bf2cdb269fc60000":
    print("\nSorry. You didn't pass the security test. Please try again.\nIf you are sure you got all of the questions correct, please notify the software distributor that gave this software to you.\n (P.S. Piss off hackers)")
    quit
else:
    print("Checksum success!")