#!/usr/bin/env python3
# example workign with Loops
#By 
#!/usr/bin/env python3
# example workign with Functions
#By Lucas Whitney 1/21/26

#prompt user to answer a question
#Store in variable
good_day_question = "Is today a good day (Y/n)"
user_response = input(good_day_question)


#if yes print a response
if user_response == "y":
    for count in range(10):
        print("Yes it is")
elif user_response =="Y":
    print("That's amazing")
else:
    print("I hope it gets better.")

