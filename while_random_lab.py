import random

x = 0
total = 0

while x < 100:
    number = random.randrange(1,10)
    print(number)

    total = total + number

    x = x + 1

number_average = total / 100

print("The sum is: ", total)
print("The average is: ", number_average)
