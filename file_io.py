loadedData = open("companies.csv", "r")

compCharCount = 0
commaCount = 0
spacesToTab = 0
for dataEntry in loadedData:
    dataEntryTabbed = ""
    for c in dataEntry:
        if commaCount == 0:
            compCharCount += 1
        if c == ",":
            if commaCount == 0:
                if compCharCount < 7:
                    spacesToTab = 7 - compCharCount
                    while spacesToTab > 0:
                        c += " "
                        spacesToTab -= 1
            commaCount += 1
            c += "\t"
        if c == ".":
            if compCharCount < 7:
                c += "\t\t"
            else:
                c += "\t"
        dataEntryTabbed += c
        compCharCount = 0
        commaCount = 0
    print(dataEntryTabbed)

print("\n")
print("Enter Company Information with the following format:")
print("\nCompany Name, Year Established, Company Headquarters\n")
print("You will need to use commas to separate fields.\n")
print("Should the company name contain commas, use\nunderscores to separate parts of the name.\n")
print("Type EXIT to finish entering any more information.\n")

recordData = open("companies.csv", "a")

newDataRecord = ""
listOfNewDataRecords = ""

while newDataRecord != "EXIT":
    newDataRecord = input("Enter Company Information: ")
    if newDataRecord != "EXIT":
        if newDataRecord.count(',') == 2:
            listOfNewDataRecords += newDataRecord
            listOfNewDataRecords += "\n"
        else:
            print("Please use the following format to enter new company information:")
            print("Company Name, Year Established, Company Headquarters")

print("Saving New Company Information...")

recordData.write(listOfNewDataRecords)
recordData.close()
