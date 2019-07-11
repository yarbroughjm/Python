employee = {"Name" : "Mark Lassoff",
            "SSN" : "000-00-0000",
            "Position" : "Founder",
            "Salary" : "$10",
            "Department" : "Instruction"}

player = {"Name" : "Bill Smith", "Team" : "Yankees", "Position" : "Pitcher"}

print(employee)
print(player)

print(employee["Name"])
print(player["Position"])

player["Position"] = "Catcher"
print("Change:", player["Position"])

del employee["Salary"]
print(employee)
