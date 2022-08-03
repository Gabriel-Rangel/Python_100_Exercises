# Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.

with open("countries_raw.txt", "r") as f:
    countries = f.readlines()
    countries = [country.strip() for country in countries]
    with open("countries.txt", "w") as new_f:
        for country in countries:
            if len(country) > 1 and country != "Top of Page":
                new_f.write(country + "\n")