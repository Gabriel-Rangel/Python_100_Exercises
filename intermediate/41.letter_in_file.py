# Create a script that generates a text file with all letters of the English alphabet 
# inside it, one letter per line.

with open("intermediate\letters.txt", "w") as f:
    for i in range(ord('a'), ord('z') + 1):
        f.write(chr(i) + "\n")