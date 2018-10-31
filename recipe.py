from course import Course
from review import Review

class Recipe:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @classmethod
    def all(cls):
        return cls._all
    @classmethod
    def top_three(cls):
        lst_top_3 = 
        for recipe in Recipe.all():
            if recipe.name ==
