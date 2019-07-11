poem = "With rue my heart is laden\n"
poem += "For golden friends I had\n"
poem += "For many a rose-lipped maiden\n"
poem += "And many a light foot lad\n"
poem += "By brooks too broad for leaping\n"
poem += "The light oot boys are laid\n"
poem += "The rose lipped girls are sleeping\n"
poem += "In fields where roses fade\n"
print(poem)

line = 1
character = 0

while character < len(poem):
    if(poem[character] != '\n'):
        currentChar = poem[character]
        if(currentChar.isupper() == True):
            print("Line: ", line, " Char: ", character, " ", currentChar, " Capital")
        else:
            print("Line: ", line, " Char: ", character, " ", currentChar)
        character = character + 1
    else:
        line = line + 1
        character = character + 1
