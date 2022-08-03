# Create a script that lets the user enter a password and checks if it is strong enough.
# A strong password is at least 5 characters long, contains at least one uppercase letter and one digit.
# Print out a message indicating whether the password is strong or not.

while True:
    notes = []
    password = input("Enter a password: ")
    if len(password)<5:
        notes.append("You need at least 5 characters")
    if not any(char.isdigit() for char in password):
        notes.append("You need at least one digit")
    if not any(char.isupper() for char in password):
        notes.append("You need at least one capital letter")
    if len(notes) == 0:
        print("Password, valid")
        break
    else:
        print("Password, invalid.")
        print("Reason(s):")
        for note in notes:
            print(note)
    print("")