"""

final project - JCR
jcroe6803@ung.edu

"""

import datetime
import time

# This program allows a user to pick a specific date and time then initializes a countdown
# until the specified date and time has been reached



month_chosen = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

# This function creates a date/time object chosen by the user and compares
# this object to the current time and provides a countdown until that chosen time
def count_down():


    year = int(raw_input('What is the year of the date? '))
    month = raw_input('What is the month of the date? ')

# this part allows the user to type in the month as a string or integer
    if len(month) < 3:
        month = int(month)
    else:   
        month = (month_strings.index(month[0:3].lower()) + 1)
    day = int(raw_input('What is the day of the month?'))
    hour = int(raw_input('What is the hour according to a 24-hour clock time?'))
    minute = int(raw_input('At which minute? '))
    second = int(raw_input('At which second? '))

    chosen_time = datetime.datetime(year,month,day,hour,minute,second)

    print 'The time chosen is: ' + chosen_time.__str__()

    current_time = chosen_time.now()
    # If the time has passed, the program provides the user with input and exits the program
    if chosen_time < chosen_time.now():
        print 'This time has elapsed.'
        exit()

    else:
        # This loop prints the amount of time remaining until the chosen time every 10 seconds
        while True:
            time_difference = (chosen_time - chosen_time.now())
            print str(time_difference) + ' until the time.'
            time.sleep(10)
            if chosen_time <= chosen_time.now():
                break
        print "Your chosen time is now! Rejoice"
        exit() 


    




    

if __name__ == '__main__':  
    count_down()   
