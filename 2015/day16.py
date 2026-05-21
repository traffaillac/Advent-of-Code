import re

ref = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def comp(s, n):
	return n > ref[s] if s in ("cats", "trees") else n < ref[s] if s in ("pomeranians", "goldfish") else n == ref[s]

for l in open(0):
	sue, a, na, b, nb, c, nc = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", l).groups()
	# part 1
	if ref[a] == int(na) and ref[b] == int(nb) and ref[c] == int(nc):
		print(sue)
	# part 2
	if comp(a, int(na)) and comp(b, int(nb)) and comp(c, int(nc)):
		print(sue)