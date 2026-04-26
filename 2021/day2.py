from sys import stdin

x, d, a = 0, 0, 0
for line in stdin:
	dir, X = line.split()
	if dir == "forward":
		x += int(X)
		d += a * int(X)
	elif dir == "down":
		a += int(X)
	else:
		a -= int(X)
print(x * d)
