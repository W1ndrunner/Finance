import csv

# Array for objects
Data = []

# Object to store info needed
class Info:
    def __init__(self, date, price):
        self.date = date
        self.price = price
    
    def getDate(self):
        return self.date
    
    def getPrice(self):
        return self.price
    
# Reading file and storing data in arrays
with open("MSFT.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        tempObj = Info(row[0], row[4])
        Data.append(tempObj)

# Deleting names of columns
del Data[0]

# Arrays to store SMA and EMA objects
SMA1 = []
SMA2 = []

EMA1 = []
EMA2 = []

# Calculates SMA
def CalcSMA(day):
    counter = day
    days = []
    for i in range(0,day):
        days.append(Data[i])
    while Data[counter] != None:
        total = 0
        for ele in days:
            total += ele.getPrice()
        SMA = total/day
        temp = Info(Data[day-1].getDate(), SMA)
        SMA1.append(temp)
        del days[0]
        days.append(Data[counter])
        counter += 1
