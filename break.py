statement = "The quick brown fox jumped over the lazy dogs."

for letter in statement:
    if letter == "s":
        break
    print("Current letter: ", letter)

for letter in statement:
    if letter == "q":
        continue
    print("Current letter: ", letter)
    
