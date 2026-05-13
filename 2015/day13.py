from collections import defaultdict
from itertools import permutations
import re

G = defaultdict(dict)
for l in open(0):
	u, sign, h, v = re.match(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", l).groups()
	G[u][v] = int(h) if sign=="gain" else -int(h)
n = len(G)

# part 1
print(max(sum(G[u][p[i-1]]+G[u][p[i-n+1]] for i,u in enumerate(p)) for p in permutations(G.keys())))

# part 2
print(max(sum((G[u][p[i-1]] if i>0 else 0)+(G[u][p[i-n+1]] if i<n-1 else 0) for i,u in enumerate(p)) for p in permutations(G.keys())))
