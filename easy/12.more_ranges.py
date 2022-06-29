# Complete the script so that it produces the expected output. 
# Please use my_range  as input data.
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

my_range = list(range(1, 21))
new_range = list()

for i in my_range:
    n = i*10
    new_range.append(n)

print(new_range)

'''
my_range = range(1, 21)
print([i*10 for i in my_range])
'''