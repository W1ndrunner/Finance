import csv

# Arrays for data needed
Dates = []
Prices = []

# Reading file and storing data in arrays
with open("MSFT.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        Dates.append(row[0])
        Prices.append(row[4])

# Deleting Names of columns
del Dates[0]
del Prices[0]

SMA = []
EMA = []


