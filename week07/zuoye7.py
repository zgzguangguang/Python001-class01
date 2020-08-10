from abc import ABC,ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,type,size,character):
        self.type = type
        self.size = size
        self.character = character
    @property
    def is_bease(self):
        if self.type == "食肉" and self.character == "凶猛" and (self.size == "中" or self.size == "大"):
            return True
        return False
class Cat(Animal):
    sound = "miao"
    def __init__(self,name,type,size,character):
        super(Cat,self).__init__(type,size,character)
        self.name = name
    @property
    def is_pet(self):
        return not self.is_bease

class Zoo(object):
    def __init__(self,animal_type):
        self.animal_type = animal_type
        self.animals = {}
    def add_animal(self,animal):
        animal_id = id(animal)
        if animal_id in self.animals:
            return
        self.animals[animal_id] = animal
        if not hasattr(self,animal):
            setattr(self,animal,[animal])
        else:
            return