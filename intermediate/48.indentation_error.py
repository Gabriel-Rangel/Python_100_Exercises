#The script is supposed to print out the letter "e" if the letter is in the string "Hello," but it doesn't. Please try to fix the script.
'''
for letter in "Hello":
    if letter == "e":
    print(letter)
'''

# Answer: The error is happening because the line with print command is not properly indented
for letter in "Hello":
    if letter == "e":
        print(letter)
