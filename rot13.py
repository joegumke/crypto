# Name: rot13.py 
# Author: Joe Gumke
# Date : 12-11-2020
# Description: Enter string to rotate characters 13 

import sys
alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = sys.argv[1]
stringLength=len(string)
offset = 13
alphaPointer=""
cipherText=""

if len(sys.argv) !=2:
    print("Please enter appropriate arguments \r\n 1.string to cipher \r\n 2.number of offset characters")
    exit()

for i in range(stringLength):
    c = string[i]
    location = alphaUpper.find(c.upper())
    alphaPointer=location + int(offset)
    if alphaPointer >=26:
        alphaPointer -=26
    cipherText +=(alphaUpper[alphaPointer])

print("Plain: ", string)
print("Cipher: ",cipherText)