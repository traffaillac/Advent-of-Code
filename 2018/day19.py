from sys import stdin

def run(code, ip):
	r = [0, 0, 0, 0, 0, 0]
	while 0 <= r[ip] < len(code):
		op, A, B, C = code[r[ip]]
		if op == 'addr': r[C] = r[A] + r[B]
		elif op == 'addi': r[C] = r[A] + B
		elif op == 'mulr': r[C] = r[A] * r[B]
		elif op == 'muli': r[C] = r[A] * B
		elif op == 'banr': r[C] = r[A] & r[B]
		elif op == 'bani': r[C] = r[A] & B
		elif op == 'borr': r[C] = r[A] | r[B]
		elif op == 'bori': r[C] = r[A] | B
		elif op == 'setr': r[C] = r[A]
		elif op == 'seti': r[C] = A
		elif op == 'gtir': r[C] = int(A > r[B])
		elif op == 'gtri': r[C] = int(r[A] > B)
		elif op == 'gtrr': r[C] = int(r[A] > r[B])
		elif op == 'eqir': r[C] = int(A == r[B])
		elif op == 'eqri': r[C] = int(r[A] == B)
		elif op == 'eqrr': r[C] = int(r[A] == r[B])
		r[ip] += 1
	return r

ip = int(input().split()[1])
code = []
for inst in stdin.readlines():
	op, A, B, C = inst.split()
	code.append((op, int(A), int(B), int(C)))
print(run(code, ip)[0])
