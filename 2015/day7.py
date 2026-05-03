from collections import defaultdict
import re

C = {} # counts the number of unresolved inputs per gate
F = {} # function to call once the given gate has all inputs resolved
A = {} # arguments passed to each function
D = defaultdict(list) # list of gates that depend on given gate
V = {} # output value per gate
S = [] # stack of gates with all resolved inputs
for l in open(0):
	if m := re.match(r"(\w+) -> (\w+)", l):
		i, x = m.groups()
		if i.isdigit():
			V[x] = int(i)
			S.append(x)
		else:
			C[x] = 1
			F[x] = lambda i: V[i]
			A[x] = (i,)
			D[i].append(x)
	elif m := re.match(r"(\w+) AND (\w+) -> (\w+)", l):
		x, y, z = m.groups()
		C[z] = 2 if x.isalpha() else 1
		F[z] = lambda x, y: (V[x] if x.isalpha() else int(x)) & V[y]
		A[z] = (x, y)
		if x.isalpha(): D[x].append(z)
		D[y].append(z)
	elif m := re.match(r"(\w+) OR (\w+) -> (\w+)", l):
		x, y, z = m.groups()
		C[z] = 2
		F[z] = lambda x, y: V[x] | V[y]
		A[z] = (x, y)
		D[x].append(z)
		D[y].append(z)
	elif m := re.match(r"(\w+) LSHIFT (\d+) -> (\w+)", l):
		p, i, q = m.groups()
		C[q] = 1
		F[q] = lambda p, i: V[p] << int(i)
		A[q] = (p, i)
		D[p].append(q)
	elif m := re.match(r"(\w+) RSHIFT (\d+) -> (\w+)", l):
		p, i, q = m.groups()
		C[q] = 1
		F[q] = lambda p, i: V[p] >> int(i)
		A[q] = (p, i)
		D[p].append(q)
	elif m := re.match(r"NOT (\w+) -> (\w+)", l):
		e, f = m.groups()
		C[f] = 1
		F[f] = lambda e: ~V[e]
		A[f] = (e,)
		D[e].append(f)
V['b'] = 46065 # part 2 insertion
while S:
	u = S.pop()
	for v in D[u]:
		C[v] -= 1
		if C[v] == 0:
			V[v] = F[v](*A[v])
			S.append(v)
print(V['a'])