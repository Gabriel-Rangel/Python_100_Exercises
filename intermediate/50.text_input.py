# The code produces an error. Please understand the error and try to fix it

'''
age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
'''

# Answer: Any input by the user is a string, so we need to convert it to an integer in this situation.
age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)
