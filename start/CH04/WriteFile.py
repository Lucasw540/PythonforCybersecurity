#!/usr/bin/env python3
# Sample script that writes to a file
# By By Lucas Whitney on 1/26/26

#Open file for Writing
hackerinfo = open("hackme.txt", "w")

#questions to collect info
print("Answer the following questions")

name =input("What is your name? ")
favorite_color = input("What is your favorite color ")
first_pet = input("What was your first's pet's name? ")
mothers_maiden_name = input("What is your mother's maiden name? ")
elementary_school = input("What elementary school did you go to?")


#Write to the file
hackerinfo.write("Name:" + name + "\n")
hackerinfo.write("Favorite color:" + favorite_color + "\n")
hackerinfo.write("First Pet:" + first_pet + "\n")
hackerinfo.write("Mother's maiden name:" + mothers_maiden_name + "\n")
hackerinfo.write("Elementary school:" + elementary_school + "\n")