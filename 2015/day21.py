from itertools import product

def win(hp0, d0, a0, hp1, d1, a1):
	while True:
		hp1 -= max(d0 - a1, 1)
		if hp1 <= 0: return True
		hp0 -= max(d1 - a0, 1)
		if hp0 <= 0: return False

Weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
Armors = [[0, 0, 0], [13, 0, 1],[31, 0, 2],[53, 0, 3],[75, 0, 4],[102, 0, 5]]
Rings = [[0, 0, 0], [25, 1, 0],[50, 2, 0],[100, 3, 0],[20, 0, 1],[40, 0, 2],[80, 0, 3]]

least = 1000
most = 0
for equipments in product(Weapons, Armors, Rings, Rings):
	if equipments[2] is equipments[3]: continue
	c = sum(e[0] for e in equipments)
	d = sum(e[1] for e in equipments)
	a = sum(e[2] for e in equipments)
	if win(100, d, a, 103, 9, 2):
		least = min(least, c)
	else:
		most = max(most, c)
print(least)
print(most)
