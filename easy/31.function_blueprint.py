#Why is there an error in the code, and how would you fix it?

'''
def foo(a=1, b=2):
    return a + b
 
x = foo - 1
'''

# Answer: at any time we didn't invoke the function, so we need to invoke the function before we can use it.
def foo(a=1, b=2):
    return a + b
 
x = foo() - 1