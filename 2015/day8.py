I = list(map(str.rstrip, open(0)))

# part 1
print(sum(len(w) - len(eval(w)) for w in I))

# part 2
print(sum(w.count('\\') + w.count('"') + 2 for w in I))