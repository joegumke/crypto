# Name: simpleCaesar.py 
# Author: Joe Gumke
# Date : 12-11-2020
# Description: Enter string to create into cipherText followed by integer which is the number of offsets you will enter (max 26)

import sys
alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = sys.argv[1]
stringLength=len(string)
offset = sys.argv[2]
alphaPointer=""
cipherText=""

if len(sys.argv) !=3:
    print("Please enter appropriate arguments \r\n 1.string to cipher \r\n 2.number of offset characters")
    exit()
if int(sys.argv[2]) > 26:
    print("Offset too Large... Max Alpha Char is 26 letters")
    exit()

for i in range(stringLength):
    c = string[i]
    location = alphaUpper.find(c.upper())
    alphaPointer=location + int(offset)
    cipherText +=(alphaUpper[alphaPointer])

print("Plain: ", string)
print("Cipher: ",cipherText)