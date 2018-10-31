from invite import Invite
from course import Course
from review import Review
from dinnerparty import DinnerParty
from guest import Guest
from recipe import Recipe
#parties
p1 = DinnerParty("Party 1")
p2 = DinnerParty("Party 2")
#guests
drake = Guest("Drake")
snoop = Guest("Snoop Dogg")
ronaldo = Guest("Ronaldo")
messi = Guest("Messi")
#recipes
salmon = Recipe("Salmon with garlic")
chicken = Recipe("Chicken with tators")
veggie = Recipe("Tofu with greens")
soup = Recipe("Clam chowder")
desert = Recipe("Lava cake")
#reviews
r1 = Review(drake, salmon, 4.8, "Delish ish ish")
r2 = Review(messi, chicken, 4.5, "Could be better")
r3 = Review(snoop, veggie, 2.2, "Where is the meat?")
