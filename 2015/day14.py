import re

pattern = r"\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
I = [tuple(map(int, re.match(pattern, l).groups())) for l in open(0)]

# part 1
print(max(2503//(f+r)*f*s + min(2503%(f+r),f)*s for s,f,r in I))

# part 2
S = [0] * len(I)
for t in range(1, 2504):
	D = [t//(f+r)*f*s+min(t%(f+r),f)*s for s,f,r in I]
	for i in range(len(I)):
		S[i] += D[i]==max(D)
print(max(S))