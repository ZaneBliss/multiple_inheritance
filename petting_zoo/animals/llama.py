from .animal import Animal
from ..movements import Walking

class Llama(Animal, Animal):

    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        self.shift = shift