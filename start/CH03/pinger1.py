#!/usr/bin/env python3
# First example of pinging from Python
# By 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

test_file = open(dir_path + "/testfile.txt","r")


#Close the file
test_file.close()