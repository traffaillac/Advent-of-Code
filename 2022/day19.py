import functools, re, sys

def rec(t, a, b, c, d, ar, br, cr, dr):
	global best
	if t<0: return
	best = max(best, d+t*dr)
	if t>1:
		if cr>0: # wait and build geode robot if possible
			td = max((da-a+ar-1)//ar, (dc-c+cr-1)//cr, 0)
			rec(t-td-1, a+(td+1)*ar-da, b+(td+1)*br, c+(td+1)*cr-dc, d+(td+1)*dr, ar, br, cr, dr+1)
		if br>0: # wait and build obsidian robot if possible
			tc = max((ca-a+ar-1)//ar, (cb-b+br-1)//br, 0)
			rec(t-tc-1, a+(tc+1)*ar-ca, b+(tc+1)*br-cb, c+(tc+1)*cr, d+(tc+1)*dr, ar, br, cr+1, dr)
		# wait and build clay robot (always possible)
		tb = max(ba-a+ar-1, 0)//ar
		rec(t-tb-1, a+(tb+1)*ar-ba, b+(tb+1)*br, c+(tb+1)*cr, d+(tb+1)*dr, ar, br+1, cr, dr)
		# wait and build ore robot (always possible)
		ta = max(aa-a+ar-1, 0)//ar
		rec(t-ta-1, a+(ta+1)*ar-aa, b+(ta+1)*br, c+(ta+1)*cr, d+(ta+1)*dr, ar+1, br, cr, dr)

R = r"""Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."""
s = 0
for T in re.findall(R, sys.stdin.read()):
	i, aa, ba, ca, cb, da, dc = map(int, T)
	best = 0
	rec(24, 0, 0, 0, 0, 1, 0, 0, 0)
	print(i, best)
	s += i * best
print(s)
