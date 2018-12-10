# finalproject_python
Final project for GISC 3200K

# Countdown Timer
This program allows a user to choose a specific date and time then initializes a countdown until the specified 
date and time has been reached. After the user has chosen a date and time, the program compares the specified time 
to the current time in order to provide an accurate countdown. If the specified date and time has passed, the program 
provides the user with input and a prompt to exit the program; otherwise, the program prints the remaining time left 
on the countdown every ten seconds until the chosen date and time has been reached. 

# Why did I choose to create the Countdown Timer?
My original project idea involved installing a third party library, mapnik, to use python coding to render a world map
with the State of Georgia highlighted as its emphasis. However, installing mapnik on the school network proved to be
infeasible. The Countdown Timer utilizes modules that reside within the Python standard library and required a skill level
that reflects my current capabilities. 

# How does the Countdown Timer work?
The time and datetime modules were imported from the Python standard library to enable this project. Used the 'DEF' function to define the 
countdown. An else statement was then combined with an if statement to allow for user input regarding the year, month, day, hour, minute,
and second. A second else statement was combined with an if statement to further initate the countdown, allowing the program to provide
the user input regarding their chosen time and the status surrounding it. At the end of of each execution of the IF/ELSE statements,
a phrase is printed informing the user of the chosen time, if the time has elapsed, or if their chosen time is commencing presently.
