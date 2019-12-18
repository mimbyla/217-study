# constructed with guidance of directions here: https://towardsdatascience.com/getting-census-data-in-5-easy-steps-a08eeb63995d

# manipulate dataframes in python

import pandas as pd

# make API calls with python

import requests

# allows us to store results of API call cleanly

import json

# construct the API call we will use

calledAPI = "https://api.census.gov/data/timeseries/poverty/saipe?get=SAEPOVRTALL_PT,SAEPOVRT0_17_PT,NAME&for=county:019,147&in=state:17&time=2018&key=f9df90bfe061e3e1734b1d91ca3e4bb9f72cb0a8"
response = requests.get(calledAPI)
listoflists = response.json()


counties = []
povrt = []

for list in listoflists:
    counties.append(list[2])
    povrt.append(list[0])

del counties[0]
del povrt[0]

count_index = 0
allrows = []

for county in counties:
    row = []
    row.append(counties[count_index])
    row.append(povrt[count_index])
    allrows.append(row)
    count_index = count_index + 1

headers = ["County_Name","Poverty_Rate"]

import csv

with open('countypov.csv','w',newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(allrows)

import numpy as np

import matplotlib.pyplot as plt


table = pd.read_csv("countypov.csv")
# print(table.head())

print(plt.bar(x=np.arange(1,3), height=table["Poverty_Rate"]))

plt.title("Poverty Rate in IL Counties")

plt.xticks(np.arange(1,3),table["County_Name"], rotation=0)
plt.xlabel("County")
plt.ylabel("Poverty Rate")
plt.show()

