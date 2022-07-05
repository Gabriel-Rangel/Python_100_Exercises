# Why is there an error in the code, and how would you fix it?
# the function doesn't return nothing, so we need to return something
'''
def foo(a, b):
    print(a + b)
 
x = foo(2, 3) * 10
'''
# code fixed
def foo(a, b):
    return a+b
 
x = foo(2, 3) * 10
