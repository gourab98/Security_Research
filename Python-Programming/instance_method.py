class dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{} says woof".format(self.name))


my_dog = dog("Amir")
my_dog.bark()
