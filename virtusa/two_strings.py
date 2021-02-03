a = ['ab','cd','ef']
b = ['af','ee','ef']
c = []
for i,j in dict(zip(a,b)).items():
    r = [True for a in i for b in j if a == b]
    if len(r) == 0:
        c.append('No')
    else:
        c.append('Yes')
for i in c:
    print(i)