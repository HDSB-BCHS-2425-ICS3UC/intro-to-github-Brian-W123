"""
Author:
Date :
Description: 
"""
import math
import time
print("Start? Yes/No")
Start= input("").lower()
#Asks user to start program and allows user to input Y/N
if Start=="yes":
 print("Beginning program...")
    #2 Second Delay
 time.sleep(2)
   #This is a float
 print("Float: ",float(1.1))
    #1 second delay to not overwhelm user
 time.sleep(1)
    #This is an integer
 print ("integer: ", int(1))
    #Another 1 second delay
 time.sleep(1)
    #This is a string
 print("String: str")

 print("Proceed to math? Yes/No")
 Proceed=input("").lower()
 if Proceed==("yes"): 
    print("Proceeding...")
    time.sleep(2)
else:
    print("either typed 'No' or something other")
#Checks if user selects yes to start

