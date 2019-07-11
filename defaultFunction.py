def employeeInformation(name = "", ssn = "000-00-000", position = ""):
    print("Name:", name)
    print("Ssn:", ssn)
    print("Position:", position)
    return

def moreEmployee(name, *other):
    print("Employee Info:")
    print("Name:", name)
    for var in other:
        print(var)
    return

employeeInformation(name = "Mark Lassoff")
moreEmployee("Mark Lassoff", "Founder", "9-1-2009", "206", "Milford")
