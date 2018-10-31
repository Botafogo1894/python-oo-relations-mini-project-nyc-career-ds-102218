class Invite:

    _all = []

    def __init__(self, dinner_party, guest):
        self._accepted = None
        self._guest = guest
        self._dinner_party = dinner_party
        Invite._all.append(self)

    @property
    def dinner_party(self):
        return self._dinner_party
    @property
    def guest(self):
        return self._guest
    @classmethod
    def all(cls):
        return cls._all
