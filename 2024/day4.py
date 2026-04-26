I = [*open(0)]
# h = sum(r.count("XMAS")+r.count("SAMX") for r in I)
# v = sum(''.join(I[r+i][c] for i in range(4)) in ("XMAS", "SAMX") for r in range(len(I)-3) for c in range(len(I[0])))
# d0 = sum(''.join(I[r+i][c+i] for i in range(4)) in ("XMAS", "SAMX") for r in range(len(I)-3) for c in range(len(I[0])-3))
# d1 = sum(''.join(I[r+i][c-i] for i in range(4)) in ("XMAS", "SAMX") for r in range(len(I)-3) for c in range(3,len(I[0])))
# print(h+v+d0+d1)
print(sum(I[r][c]+I[r][c+2]+I[r+1][c+1]+I[r+2][c]+I[r+2][c+2] in ("MMASS", "MSAMS", "SMASM", "SSAMM") for r in range(len(I)-2) for c in range(len(I[0])-2)))