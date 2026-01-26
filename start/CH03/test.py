#!/usr/bin/env python3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

test_file = open(dir_path + "/testfile.txt","w")

#Write Line to a file
print("Hello world")
print("have a good day")
test_file.write("Hello There\n")
test_file.write("Nice to see you\n")
test_file.write("Come back again")
#Close the file
test_file.close()