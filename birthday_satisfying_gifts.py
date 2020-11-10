test_cases = int(input('enter the testcases : '))
d = {}
for i in range(test_cases):
    i = int(input('frnd length : '))
    l = []
    for a in range(i):
        a = int(input('frnd : '))
        l.append(a)
    factor = int(input('enter factor : '))    
    d[factor] = l
print(d)
new_d = {}
for i,j in d.items():
    a = sorted(j,reverse=False)
    new_d[i] = a
print(new_d)
# res = {}
# for i,j in new_d.items():
#     ca = len(j) * j[0]
#     if i == 1:
#         res[i] = ca
# for i,j in res.items():
#     print(j)