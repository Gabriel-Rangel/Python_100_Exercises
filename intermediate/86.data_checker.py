# Please take a look at the following list:
checklist = ["Portugal", "Germany", "Munster", "Spain"]
# One of the items is not a country. 
# Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. 
# Once you have filtered out checklist , then print it out.

with open("countries.txt", "r") as f:
    countries = f.readlines()
    countries = [country.strip() for country in countries]
    list_checked = []
    for country in countries:
        if country in checklist:
            list_checked.append(country)

print(list_checked)

