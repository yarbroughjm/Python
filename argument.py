#Function definition
def greetMe(str):
    #This function greets the name passed in
    print("Welcome to the function", str)
    return

def calculateBattingAverage(atBats, hits, walks):
    #This function calculates batting average
    battingAverage = hits/(atBats-walks)
    print(battingAverage)

#Function Calls
greetMe("Kevin")
greetMe("Brett")
calculateBattingAverage(200,54,12)
calculateBattingAverage(300,108,6)
