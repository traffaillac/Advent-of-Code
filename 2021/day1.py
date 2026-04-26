from sys import stdin
from math import inf

count = 0
a = int(next(stdin))
b = int(next(stdin))
c = int(next(stdin))
for d in map(int, stdin):
	count += a + b + c < b + c + d
	a, b, c = b, c, d
print(count)
