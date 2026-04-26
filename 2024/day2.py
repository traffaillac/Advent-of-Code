safe = lambda L:(L==sorted(L) or L==sorted(L,reverse=True)) and all(1<=abs(a-b)<=3 for a, b in zip(L, L[1:]))
I = [list(map(int, l.split())) for l in open(0)]
print(sum(safe(L) or any(safe(L[:i]+L[i+1:]) for i in range(len(L))) for L in I))
