#!/usr/bin/env python3
# Sample script that reads from a file
# By Lucas Whitney 1/26/26
#open file for reading

hackerinfo = open("hackme.txt", "r")

#Read file and print to screen

contents = hackerinfo.read()
print(contents + "Here's someone to hack -information")