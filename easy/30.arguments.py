# Why do you get an error, and how would you fix it?
'''
def foo(a=2, b):
    return a + b
'''

# Answer: arguments with default values must be placed after all other arguments.
# The code will not work if you place the default value before the other arguments.

def foo(a, b=2):
    return a + b