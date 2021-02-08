# Convert the human readable date to epoch timestamp/time as on the start of the day?
# Example.
# If the INPUT date is 21-01-2020, print the epoch time at the start of the day i.e 12:00 AM
# Conditions:
# Date limit: 01-01-1970 to <the date of execution of the test cases>
# Input Description:
# The input date will be in any of the following format.
# 1) dd/mm/yyyy
# 2) mm/dd/yyyy
# 3) dd-mm-yyyy
# 4) mm-dd-yyyy
# 5) dd.mm.yyyy
# 6) mm.dd.yyyy
# 7) ddmmyyyy
# 8) mmddyyyy
# Output Description:
# For all the types of above input date, the output should be an Epoch timestamp/time.
# Question 1 – Date to Epoch timestamp

# Exceptions:
# Any input date other than the given formats must be handled and a message "Unable to convert the
# provided date" must be printed.
# More Examples:
# Example 1
# Input: 19-01-2020
# Output: 1579392000
# Example 2
# Input: 31122012
# Output: 1356912000
# Example 3
# Input: 251220202
# Output: Unable to convert the provided date
# Example 4
# Input: 17:04:2020
# Output: Unable to convert the provided date


import datetime
myDate = input('Enter your date :')
if myDate[2] == '/' and int(myDate[3:5]) < 13 :
    try:
        print(datetime.datetime.strptime(myDate, "%d/%m/%Y").timestamp())
    except:
        print('Unable to convert the provided data')
elif myDate[2] == '/' and int(myDate[3:5]) > 12 :
    try:
        print(datetime.datetime.strptime(myDate, "%m/%d/%Y").timestamp())
    except :
        print('Unable to convert the provided data')
elif myDate[2] == '-' and int(myDate[3:5]) < 13 :
    try:
        print(datetime.datetime.strptime(myDate, "%d-%m-%Y").timestamp())
    except :
        print('Unable to convert the provided data')
elif myDate[2] == '-' and int(myDate[3:5]) > 12 :
    try:
        print(datetime.datetime.strptime(myDate, "%m-%d-%Y").timestamp())
    except :
        print('Unable to convert the provided data')
elif myDate[2] == '.' and int(myDate[3:5]) < 13 :
    try:
        print(datetime.datetime.strptime(myDate, "%d.%m.%Y").timestamp())
    except :
        print('Unable to convert the provided data')
elif myDate[2] == '.' and int(myDate[3:5]) > 12 :
    try:
        print(datetime.datetime.strptime(myDate, "%m.%d.%Y").timestamp())
    except:
        print('Unable to convert the provided data')
elif int(myDate[0:2]) <30  and int(myDate[2:4]) < 13 :
    try:
        print(datetime.datetime.strptime(myDate, "%d%m%Y").timestamp())
    except:
        print('Unable to convert the provided data')
elif int(myDate[0:2]) < 13  and int(myDate[2:4]) > 12 :
    try:
        print(datetime.datetime.strptime(myDate, "%m%d%Y").timestamp())
    except:
        print('Unable to convert the provided data')
else:
    print('Unable to convert the provided data')