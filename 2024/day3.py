import re
# print(sum(int(a)*int(b) for a,b in re.findall(r"mul\((\d+),(\d+)\)", open(0).read())))
I = open(0).read()
s = 0
on = True
for i in range(len(I)):
	if I[i:].startswith("do()"):
		on = True
	elif I[i:].startswith("don't()"):
		on = False
	else:
		m = re.match(r"mul\((\d+),(\d+)\)", I[i:])
		if m:
			s += int(m.group(1))*int(m.group(2))*on
print(s)