class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList
        
    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return num
    
    def avg(self):
        result = 0
        for num in self.numberList:
            result += num    
        average = result / len(self.numberList)
        return average

cal = Calculator([1, 2, 3, 4, 5])
print(cal.sum())
print(cal.avg())