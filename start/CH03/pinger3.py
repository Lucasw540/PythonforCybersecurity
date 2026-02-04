#!/usr/bin/env python3
# Third example of pinging from Python
# By Lucas Whitney 2/4/26

def send_message():
    for x in range(10):
        print("Yeah it is")


#ask user if today is a good day
if input("Is today a good day(y/n)") == "y":
    send_message()
