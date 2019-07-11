family = ("Joan", "Rick", "Brett", "Kerri", "Rose", "Stacy")
print(family)
print(family[0])
print(family[5])

#Looping through the Tuple
x = 0
while x < 6:
    print(family[x])
    x = x + 1

#Don't do this!
family[1] = "Ricky"
