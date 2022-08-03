from operator import index
import requests
import pandas as pd
'''
f1 = requests.get("https://pythonhow.com/media/data/sampledata.txt").text
with open("sampledata.txt", "w") as f:
    f.write(f1)
f2 = requests.get("https://pythonhow.com/media/data/sampledata_x_2.txt")
with open("sampledata2.txt", "w") as f:
    f.write(f1)
'''
df1 = pd.read_csv("sampledata.txt")
df2 = pd.read_csv("sampledata2.txt")
df = pd.concat([df1, df2])
print(df)