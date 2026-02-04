#!/usr/bin/env python3
# example workign with Functions
#By Lucas Whitney 1/21/26

#prompt user to answer a question
#Store in variable
#This is my function
def print_me( my_message):
    print("my_message")
    return "it worked!"

def say_hello(num_times):
    for x in range(num_times):
        print("Hello World")

 
 
 #Calling the Function
 
 
print_me("This is a function")
result = print_me("This is another function with a return value")
print(result)
say_hello(3)

good_day_question = "Is today a good day (Y/n)"
user_response = input(good_day_question)


#if yes print a response
if user_response == "y":
    print("Yes it is")
elif user_response =="Y":
    print("That's amazing")
else:
    print("I hope it gets better.")


