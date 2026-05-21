I = tuple(map(int, open(0)))

def count(i, e, m):
	return 0 if m==0 else sum((1 if I[j]==e else count(j+1, e-I[j], m-1)) for j in range(i, len(I)) if I[j]<=e)

# part 1
print(count(0, 150, len(I)))

# part 2
m = 1
while (c := count(0, 150, m)) == 0:
	m += 1
print(c, m)