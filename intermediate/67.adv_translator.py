# Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary 
# as a vocabulary source. 
# In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.


d = dict(weather = "clima", earth = "terra", rain = "chuva")
w = input("Enter a word: ").lower()
wp = d.get(w)

print(wp if wp else "We couldn't find that word!")