# part 1
N = 1000000
houses = [0] * N
for elf in range(1, N):
	for house in range(elf, N, elf):
		houses[house] += elf
	if houses[elf] >= 3400000:
		print(elf)
		exit()

# part 2
N = 1000000
houses = [0] * N
for elf in range(1, N):
	for house in range(elf, min(N, 51*elf), elf):
		houses[house] += elf
	if houses[elf] >= 3090910:
		print(elf)
		exit()
