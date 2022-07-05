# Create a script that generates a file where all letters of the English alphabet are listed two in each line. 
# The inside of the text file would look like:

with open("intermediate\letters_2by2.txt", "w") as f:
    for i in range(ord('a'), ord('z') + 1, 2):
        f.write(chr(i) + chr(i+1) + "\n")
        