from collections import defaultdict
from itertools import permutations
import re

G = defaultdict(dict)
for l in open(0):
	u, v, d = re.match(r"(\w*) to (\w*) = (\d*)", l).groups()
	G[u][v] = G[v][u] = int(d)

# part 1
print(min(sum(G[u][v] for u, v in zip(p, p[1:])) for p in permutations(G.keys())))

# part 2
print(max(sum(G[u][v] for u, v in zip(p, p[1:])) for p in permutations(G.keys())))
