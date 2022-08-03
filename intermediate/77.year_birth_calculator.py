#Create a script that asks the user to enter their age, 
# and the script calculates the user's year of birth and prints it out in a string like in the expected output. 
# 'We think you were born back in 1988'
# Please make sure you generate the current year dynamically.

import datetime

age = int(input("Enter your age: "))
year = datetime.datetime.now().year - age

print(f"We think you were born back in {year}")
