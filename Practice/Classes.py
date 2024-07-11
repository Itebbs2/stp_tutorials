"""
A script for practicing using classes
"""

class Animal:
    def __init__(self, name, colour, diet, habitat):
        self.name = name
        self.colour = colour
        self.diet = diet
        self.habitat = habitat
    def print_name(self):
        print(self.name)
    def summary(self):
        """
        provides a summary of a given animal
        :return:
        """
        print(f'The {self.name} is a {self.colour} animal, it'
              f' lives in the {self.habitat} and eats {self.diet} \n')

"""
Listing all of the animals and their details
"""
Giraffe = Animal("Giraffe", "yellow", "leaves", "Savannah")
Panda = Animal("Panda", "black and white", "bamboo", "Chinese mountains")



Animal.summary(Giraffe)
Animal.summary(Panda)