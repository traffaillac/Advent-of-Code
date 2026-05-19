import re

I = [tuple(map(int, re.match(r"\w+: capacity ([-+]?\d+), durability ([-+]?\d+), flavor ([-+]?\d+), texture ([-+]?\d+), calories ([-+]?\d+)", l).groups())) for l in open(0)]

S = 0
for n in range(100 ** (len(I)-1)):
	Q = [n//100**i%100 for i in range(len(I)-1)]
	Q.append(100 - sum(Q))
	# remove second condition for part 1
	if Q[-1] >= 0 and sum(q*cl for q, (cp, d, f, t, cl) in zip(Q, I)) == 500:
		CP, D, F, T = 0, 0, 0, 0
		for q, (cp, d, f, t, cl) in zip(Q, I):
			CP += q * cp
			D += q * d
			F += q * f
			T += q * t
		S = max(S, max(CP,0) * max(D,0) * max(F,0) * max(T,0))
print(S)