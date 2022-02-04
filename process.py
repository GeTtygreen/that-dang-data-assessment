# here were opening and looping over a file 
log_file = open("um-server-01.txt")

# here were creating a function including the file we opened to use its data
def sales_reports(log_file):
    # now begins the loop 
    for line in log_file:
        # here removing the whitespace and trailing charcters 
        line = line.rstrip()
        # identifing the index position of the object we want to work with 
        day = line[0:3]
        # creating a condition stating that if the object is tue print /display it in the console naked/just the word without any whitespace or trailing charcters
        if day == "Tue":
            print(line)
            # prints the day mon or tues naked alont with the sales info for those dates 
        elif day == "Mon":
            print(line)
            # states that if the day is not mon or tues just console the actual day naked 
        else:
            print(day)
        
            

# invoking the function that was created on to the file that was open 
sales_reports(log_file)
