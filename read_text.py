myfile = open("employees.txt", "r")
#print (myfile.read(15))
#print (myfile.readline())
#print (myfile.readline(3))
for line in myfile:
    thisline = line
    print("1:", line)
