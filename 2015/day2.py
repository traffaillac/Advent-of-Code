I = open(0).readlines()

# day 1
a = 0
for s in I:
	l, w, h = map(int, s.split('x'))
	a += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(a)

# day 2
r = 0
for s in I:
	l, w, h = map(int, s.split('x'))
	r += 2*min(l+w, w+h, h+l) + l*w*h
print(r)
