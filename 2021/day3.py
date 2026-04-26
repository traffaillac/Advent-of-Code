from statistics import median_high
from sys import stdin

diag = list(line.rstrip() for line in stdin)
gamma = int(''.join(map(str, (int(median_high(int(bits[i]) for bits in diag)) for i in range(len(diag[0]))))), 2)
print(gamma * (gamma ^ ((1 << gamma.bit_length()) - 1)))

oxy = diag
for i in range(len(diag[0])):
	mcv = str(int(median_high(int(bits[i]) for bits in oxy)))
	oxy = list(filter(lambda bits: bits[i]==mcv, oxy))
scr = diag
for i in range(len(diag[0])):
	counts = [sum(w[i]=='0' for w in scr), sum(w[i]=='1' for w in scr)]
	lcv = '0' if 0<counts[0]<=counts[1] or counts[1]==0 else '1'
	scr = list(filter(lambda bits: bits[i]==lcv, scr))
print(int(oxy[0], 2) * int(scr[0], 2))
