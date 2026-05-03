I = input()
def move(x, y, c):
	dx, dy = [(0, 1), (0, -1), (1, 0), (-1, 0)]['^v><'.index(c)]
	x += dx
	y += dy
	return x, y

# part 1
x, y = 0, 0
S = {(0, 0)}
for c in I:
	x, y = move(x, y, c)
	S.add((x, y))
print(len(S))

# part 2
x, y, X, Y = 0, 0, 0, 0
S = {(0, 0)}
for c, d in zip(I[::2], I[1::2]):
	x, y = move(x, y, c)
	X, Y = move(X, Y, d)
	S |= {(x, y), (X, Y)}
print(len(S))
