from itertools import product
from pprint import pprint
from sys import stdin

numbers = map(int, next(stdin).split(','))
boards = []
try:
	while True:
		next(stdin)
		boards.append([list(map(int, next(stdin).split())) for _ in range(5)])
except:
	pass

marks = [set() for _ in boards]
for n in numbers:
	i = 0
	while i < len(boards):
		b, m = boards[i], marks[i]
		if any(n in l for l in b):
			m.add(n)
		if any(all(b[r][c] in m for c in range(5)) for r in range(5)) or \
		   any(all(b[r][c] in m for r in range(5)) for c in range(5)):
			print(sum(b[r][c] for r, c in product(range(5), repeat=2) if b[r][c] not in m) * n)
			del boards[i], marks[i]
		else:
			i += 1
