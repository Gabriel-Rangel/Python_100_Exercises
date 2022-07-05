#Create a function that takes any string as input 
# and returns the number of words for that string.

def count_words(string):
    return len(string.split())

print(count_words("Hey there it's me!"))