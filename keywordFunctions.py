def greetTwoPeople(person1, person2):
    #This function greets two people
    print("Greetings", person1)
    print("Hello, How are you?", person2)
    return

def calculateBa(atBats, hits, walks):
    ba = hits/(atBats - walks)
    print(ba)
    return

greetTwoPeople(person2 = "Brett", person1 = "Mark")
calculateBa(atBats=317, hits=67, walks=25)
