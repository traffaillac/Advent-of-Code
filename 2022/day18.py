import sys

# part 1
C = {tuple(map(int, l.split(','))) for l in sys.stdin.read().splitlines()}
D = ((-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1))
print(sum((x+i,y+j,z+k) not in C for i, j, k in D for x, y, z in C))

# part 2
mx, my, mz = min(x for x,y,z in C)-1, min(y for x,y,z in C)-1, min(z for x,y,z in C)-1
Mx, My, Mz = max(x for x,y,z in C)+1, max(y for x,y,z in C)+1, max(z for x,y,z in C)+1
L, S, e = [(mx, my, mz)], {(mx, my, mz)}, 0
while L:
	x, y, z = L.pop()
	for i, j, k in D:
		if mx<=x+i<=Mx and my<=y+j<=My and mz<=z+k<=Mz:
			if (x+i, y+j, z+k) in C:
				e += 1
			elif (x+i, y+j, z+k) not in S:
				L.append((x+i, y+j, z+k))
				S.add((x+i, y+j, z+k))
print(e)
