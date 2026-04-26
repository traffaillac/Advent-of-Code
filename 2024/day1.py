I = [*open(0)]
# A = sorted(int(l.split()[0]) for l in I)
# B = sorted(int(l.split()[-1]) for l in I)
# print(sum(abs(a-b) for a, b in zip(A, B)))
A = [int(l.split()[0]) for l in I]
B = [int(l.split()[-1]) for l in I]
print(sum(a*B.count(a) for a in A))
