from hashlib import md5

# part 1
for i in range(1000000000):
	if md5(b'ckczppom'+str(i).encode(), usedforsecurity=False).hexdigest().startswith('00000'):
		print(i)
		break

# part 2
for i in range(1000000000):
	if md5(b'ckczppom'+str(i).encode(), usedforsecurity=False).hexdigest().startswith('000000'):
		print(i)
		break
