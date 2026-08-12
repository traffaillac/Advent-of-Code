instructions = open(0).read().split('\n')
ip = 0
regs = {'a': 1, 'b': 0} # set a to 0 for part 0
while 0 <= ip < len(instructions):
	op, params = instructions[ip].split(' ', maxsplit=1)
	ip += 1
	if op == "hlf":
		regs[params] >>= 1
	elif op == "tpl":
		regs[params] *= 3
	elif op == "inc":
		regs[params] += 1
	elif op == "jmp":
		ip += int(params) - 1
	elif op == "jie":
		reg, off = params.split(", ")
		ip += int(off) - 1 if regs[reg] % 2 == 0 else 0
	elif op == "jio":
		reg, off = params.split(", ")
		ip += int(off) - 1 if regs[reg] == 1 else 0
print(regs)