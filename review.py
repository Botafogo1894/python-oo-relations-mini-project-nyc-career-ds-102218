class Review:

    _all = []

    def __init__(self, reviewer, recipe, rating, comment):
        self._rating = rating
        self._recipe = recipe
        self._reviewer = reviewer
        self._comment = comment
        Review._all.append(self)

    @classmethod
    def top_3_avg_rating(cls):
        full = list(map(lambda item: dict(recipe = recipe, rating = rating)))
    @property
    def reviewer(self):
        return self._reviewer
    @property
    def recipe(self):
        return self._recipe
    @property
    def rating(self):
        return self._rating
    @property
    def comment(self):
        return self._comment
    @classmethod
    def all(cls):
        return cls._all
