I = open(0).read().split()

# part 1
def isnice1(w):
	return sum(c in "aeiou" for c in w)>=3 and any(a==b for a, b in zip(w, w[1:])) and all(s not in w for s in ["ab", "cd", "pq", "xy"])
print(sum(isnice1(w) for w in I))

# part 2
def isnice2(w):
	return any(w[i:i+2] in w[i+2:] for i in range(len(w)-1)) and any(a==b for a, b in zip(w, w[2:]))
print(sum(isnice2(w) for w in I))
