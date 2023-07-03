import csv
Dates = []
Prices = []
with open("MSFT.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        Dates.append(row[0])
        Prices.append(row[4])

del Dates[0]
del Prices[0]



