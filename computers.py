computers = ("IBM PC", "Apple Mac", "Compaq", "Gateway", "HP", "Toshiba")
websites = ["Yahoo!", "Google", "Alta Vista", "Dog Pile", "CNN"]

print(len(computers))

x = 0
while x < len(computers):
    print(computers[x])
    x = x + 1

scores = (10500, 12000, 11000, 15000, 9000, 950)
print("Min:", min(scores))
print("Max:", max(scores))

print(tuple(websites))

websites = tuple(websites)
websites[0] = "Bing"
