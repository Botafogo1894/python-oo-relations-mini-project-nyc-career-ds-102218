from invite import Invite
from course import Course

class DinnerParty:

    def __init__(self, name):
        self._name = name

        @property
        def name(self):
            return self._name
        @classmethod
        def all(cls):
            return cls._all
