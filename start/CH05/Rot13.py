#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Lucas Whitney

#Prompt for the source meessage
source_message = input("What is the message to encrypt/decript")
#Convert message to lower-case for simplicity
source_message = source_message.lower()
final_message = ""
#Loop through each letter in source message
for letter in source_message:
    #Convert the letter to the ASCII equivelent
    ascii_num = ord(letter)
    #Check to see if an alphabetic (a-z) character, if not, skip
    if ascii_num >= 97 and ascii_num <=122:
        #Add 13 to ascii-num to "shift" it by  13
        new_ascii = ascii_num + 13
        #Confirm new character will be alphabetic
    if new_ascii > 122: 
            #If not, wrap around
            new_ascii =new_ascii - 26
            final_message = final_message + chr(new_ascii)
else:
    final_message = final_message + chr(ascii_num)
#print converted message
print ("message has been converted")
print(final_message)
