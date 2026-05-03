import re
I = open(0).readlines()

# part 1
G = [0] * 1000
for l in I:
	x0, y0, x1, y1 = map(int, re.findall(r"(\d+)", l))
	mask = ((1 << (x1 - x0 + 1)) - 1) << x0
	if l.startswith("turn on"):
		for y in range(y0, y1+1):
			G[y] |= mask
	elif l.startswith("turn off"):
		for y in range(y0, y1+1):
			G[y] &= ~mask
	else:
		for y in range(y0, y1+1):
			G[y] ^= mask
print(sum(r.bit_count() for r in G))

# part 2
G = [[0]*1000 for _ in range(1000)]
for l in I:
	x0, y0, x1, y1 = map(int, re.findall(r"(\d+)", l))
	if l.startswith("turn on"):
		for y in range(y0, y1+1):
			for x in range(x0, x1+1):
				G[y][x] += 1
	elif l.startswith("turn off"):
		for y in range(y0, y1+1):
			for x in range(x0, x1+1):
				G[y][x] = max(G[y][x]-1, 0)
	else:
		for y in range(y0, y1+1):
			for x in range(x0, x1+1):
				G[y][x] += 2
print(sum(sum(r) for r in G))
