animals = ["Lion", "Dolphin", "Zebra", "Monkey"]
char = 0
for animal in animals:
    char = char + len(animal)

print("Total characters: {}, Average length: {}".format(char,char/len(animals)))