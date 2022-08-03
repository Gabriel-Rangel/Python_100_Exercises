# Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate(word):
    translation = d.get(word.lower())
    if translation is None:
        return "The word doesn't exist in the dictionary."
    return translation

print(translate(input("Enter a word: ")))