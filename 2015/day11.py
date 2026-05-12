def decode(s):
	return sum((ord(c)-ord('a'))*26**i for i,c in enumerate(reversed(s)))

def encode(n):
	return ''.join(chr(n//26**i%26+ord('a')) for i in range(7,-1,-1))

incs = [chr(i)+chr(i+1)+chr(i+2) for i in range(ord('a'), ord('y'))]
pairs = [chr(i)+chr(i) for i in range(ord('a'), ord('z')+1)]
def valid(s):
	return any(w in s for w in incs) and all(c not in s for c in "iol") and sum(w in s for w in pairs)>=2

# part 1
p = "vzbxkghb"
while not valid(p):
	p = encode(decode(p)+1)
print(p)

# part 2
p = encode(decode(p)+1)
while not valid(p):
	p = encode(decode(p)+1)
print(p)
