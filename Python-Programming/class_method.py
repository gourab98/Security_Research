class dog:
    all_dogs = []

    def __init__(self,name):
        self.name= name
        dog.all_dogs.append(self)

    @classmethod
    def total_dogs(cls):
        print()