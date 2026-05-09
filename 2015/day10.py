def lookAndSay(S):
	R = ''
	start = 0
	for i, c in enumerate(S):
		if i+1==len(S) or S[i+1]!=c:
			R += str(i+1-start) + S[i]
			start = i+1
	return R

s = '3113322113'
for i in range(50):
	s = lookAndSay(s)
print(len(s))