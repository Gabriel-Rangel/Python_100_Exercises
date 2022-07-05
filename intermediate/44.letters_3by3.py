with open("intermediate\letters_3by3.txt", "w") as f:
    for i in range(ord('a'), ord('z') + 1, 3):
        f.write(chr(i) + chr(i+1) + chr(i+2) + "\n")