from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return Guest._all
        
