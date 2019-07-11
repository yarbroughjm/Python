gpas = (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)
#gpas[1] = 2.25

gpas_total = 0
x = 0
while x < len(gpas):
    gpas_total = gpas_total + gpas[int(x)]
    x = x + 1

gpas_average = gpas_total / len(gpas)
print("The average of GPAs:", gpas_average, "\n")

#gpas_dictionary = {"Name" : ("Bob", "Mark", "Morton", "Travis", "DeeDee", "Ian"), "GPA" : (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)}
#print(gpas_dictionary)
##print(gpas_dictionary['Name'])
##
##for k, v in gpas_dictionary.items():
##    for y in len(gpas_dictionary.items()):
    #for y in v:
##        for z in k:
##            print(y, z)
##        print(gpasdictionary[k[y], v[y]])
##    for y in v:
##        print(v[int(y)])
    #print(k, v)
    #print(k[int(k)], v[int(k)])
##    for y in len(k):
##        print(v[y])

gpas_dictionary = {'Bob' : 3.14, 'Mark' : 3.45, 'Morton' : 3.98, 'Travis' : 2.55, 'DeeDee' : 3.24, 'Ian' : 2.27}

gpas_loop_total = 0

for k, v in gpas_dictionary.items():
    gpas_loop_total = gpas_loop_total + v
    #print(k, ": \t\t", v, sep = "")
    #print("{0:0}{1:12}".format(k + ":", v))
    if v == max(gpas_dictionary.values()):
        gpasMaxStudent = k
        gpasMax = v
    elif v == min(gpas_dictionary.values()):
        gpasMinStudent = k
        gpasMin = v
    print('{0:8}{1:>6}'.format(k + ":", v))
gpas_loop_average = gpas_loop_total / len(gpas_dictionary)
print("\nAverage GPA:", gpas_loop_average)

#gpasMax = max(gpas_dictionary.values())
print("The maximum GPA of ", gpasMax, " was earned by ", gpasMaxStudent, ".", sep = "")
print("The minimum GPA of ", gpasMin, " was earned by ", gpasMinStudent, ".", sep = "")
