from collections import defaultdict
from pprint import pprint
import re

rules, mol = open(0).read().rstrip().split("\n\n")

# part 1
R = [re.match(r"(\w+) => (\w+)", r).groups() for r in rules.split('\n') if r[0]!='e']
E = {r[5:] for r in rules.split('\n') if r[0]=='e'}
S = set()
for u, v in R:
	for m in re.finditer(u, mol):
		S.add(mol[:m.start()]+v+mol[m.end():])
print(len(S))

# part 2
nmol = sum(c.isupper() for c in mol)
nRn, nY, nAr = mol.count("Rn"), mol.count("Y"), mol.count("Ar")
print(nmol - 1 - nRn - nY * 2 - nAr)
