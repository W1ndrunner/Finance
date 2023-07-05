import csv

# Array for objects
Data = []

# Object to store info needed
class Info:
    def __init__(self, date, price):
        self.date = date
        self.price = float(price)
    
    def getDate(self):
        return self.date
    
    def getPrice(self):
        return self.price
    
# Reading file and storing data in arrays
with open("MSFT.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == 'Date':
            continue
        tempObj = Info(row[0], row[4])
        Data.append(tempObj)


# Arrays to store SMA and EMA objects
SMA1 = []
SMA2 = []

tempSMA = []
EMA1 = []
EMA2 = []

# Calculates SMA and stores the results as objects
def CalcSMA(day, selector):
    counter = day
    days = []
    for i in range(0,day):
        days.append(Data[i])
    while counter < len(Data):
        total = 0
        for ele in days:
            total += ele.getPrice()
        SMA = total/day
        temp = Info(Data[day-1].getDate(), SMA)
        if selector == 1:
            SMA1.append(temp)
        elif selector == 2:
            SMA2.append(temp)
        else:
            tempSMA.append(temp)
            break ## Calculating only one SMA to start the EMA calculation
        del days[0]
        days.append(Data[counter])
        counter += 1

# CalcSMA(50, 3)
# print(tempSMA[0].getPrice())

# Calculates EMA and stores the results as objects
def CalcEMA(day, selector):
    weight = 2 / (day + 1)
    counter = 1
    counter2 = day
    CalcSMA(day, 3)
    if selector == 1:
        EMA1[0] = tempSMA[0]
    else:
        EMA2[0] = tempSMA[0]
    while counter2 < len(Data):
        EMA = (Data[counter2].getPrice() * weight) + EMA1[counter-1] * (1 - weight)
        temp = Info(Data[counter2].getDate(), EMA)
        if selector == 1:
            EMA1[counter] = temp
        else:
            EMA2[counter] = temp
        counter += 1
        counter2 += 1
