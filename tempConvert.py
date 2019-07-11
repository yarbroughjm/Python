def fToC(fTemp):
    cTemp = (fTemp - 32) / 1.8
    return cTemp

def cToF(cTemp):
    fTemp = cTemp * 1.8 + 32
    return fTemp

def convertTemp(degrees, convertTo = 0):
    if convertTo > 1:
        print("Very funny! Please input a 0 (for degrees C) or a 1 (for degrees F) for the \nsecond function parameter.")
    if convertTo < 0:
        print("Very funny! Please input a 0 (for degrees C) or a 1 (for degrees F) for the \nsecond function parameter.")
    if convertTo == 1:
        convertedTemp = degrees * 1.8 + 32
        print(degrees, "degrees C =", convertedTemp, "degrees F")
    else:
        convertedTemp = (degrees - 32) / 1.8
        print(degrees, "degrees F =", convertedTemp, "degrees C")
    return convertedTemp

#fahrTemp = 212
#celsTemp = fToC(fahrTemp)
#print(fahrTemp, "degrees F =", celsTemp, "degrees C")

#celsTemp = 100
#fahrTemp = cToF(celsTemp)
#print(celsTemp, "degrees C =", fahrTemp, "degrees F")

convertTemp(100, 1)
