#nacisnij enter aby zlamac ciasteczko
#trach
#1z5 wrozb

import random

input("nacisnij ENTER, ciasteczko")
print("trrrrach\noto twoja wrozba:")

wrozba = random.randint(1,5)
if wrozba == 1:
	print("zjesz ciastko")
elif wrozba == 2:
	print("zwrocisz ciastko")
elif wrozba == 3:
	print("ciastko zje ciebie")
elif wrozba == 4:
	print("cygan zabierze ci ciastko")
elif wrozba == 5:
	print("ciastko nie istnieje")
else:
	print("ciastkowy potwor nie chce zyc na takim swiecie")
