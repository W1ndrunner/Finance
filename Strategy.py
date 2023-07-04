import csv

# Array for objects
Data = []
class Info:
    def __init__(self, date, price):
        self.date = date
        self.price = price
# Reading file and storing data in arrays
with open("MSFT.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        tempObj = Info(row[0], row[4])
        Data.append(tempObj)

# Deleting Names of columns
del Data[0]


#Arrays to store SMA and EMA objects
SMA1 = []
SMA2 = []

EMA1 = []
EMA2 = []


