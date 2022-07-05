# Write a script that extracts letters from 26 text files and put the letters in a list
# if the letters is in string "python"

letters = []
for i in range(ord('a'), ord('z') + 1):
    with open(f"intermediate\{chr(i)}.txt", "r") as f:
        letter = f.read()
        if letter in "python":
            letters.append(letter)

print(letters)