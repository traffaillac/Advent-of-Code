G = list(map(list, open(0).read().split()))
R, C = len(G), len(G[0])
G[0][0] = G[0][C-1] = G[R-1][0] = G[R-1][C-1] = '#' # comment this line for part 1
for _ in range(100):
	new = []
	for r, g in enumerate(G):
		s = []
		for c, l in enumerate(g):
			n = sum(G[r+dr][c+dc]=='#' for dr, dc in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)) if 0<=r+dr<R and 0<=c+dc<C)
			s.append('#' if l=='#' and 2<=n<=3 or l=='.' and n==3 else '.')
		new.append(s)
	G = new
	G[0][0] = G[0][C-1] = G[R-1][0] = G[R-1][C-1] = '#' # comment this line for part 1
print(sum(g.count('#') for g in G))