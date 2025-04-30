class Apple: 
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def _str_(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)


        