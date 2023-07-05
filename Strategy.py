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
            counter = len(Data)
        del days[0]
        days.append(Data[counter])
        counter += 1

CalcSMA(10, 1)
print(SMA1[0].getPrice())
