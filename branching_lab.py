subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]

if(subjectList[0] == "Geography"):
    takingGeography = "true"
elif(subjectList[1] == "Geography"):
    takingGeography = "true"
elif(subjectList[2] == "Geography"):
    takingGeography = "true"
elif(subjectList[3] == "Geography"):
    takingGeography = "true"
elif(subjectList[4] == "Geography"):
    takingGeography = "true"
else:
    takingGeography = "false"

print(takingGeography)

if(((gpas[0] + gpas[1] + gpas[2]) / 3) >= 3.33):
    print("Average is 3.33 or greater")
else:
    print("Average is less than 3.33")

print('Average is 3.33 or greater' if ((gpas[0] + gpas[1] + gpas[2]) / 3) >= 3.33 else 'Average is less than 3.33')
