I = input()

# day 1
print(sum(1 if c=='(' else -1 for c in I))

# day 2
f = 0
for i, c in enumerate(I):
	f += 1 if c=='(' else -1
	if f < 0:
		print(i+1)
		exit()
