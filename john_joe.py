test_cases = int(input('no of test cases : '))
test = [int(input()) for i in range(test_cases)]
games = []
for i in test:
    i = [input() for a in range(i)]
    games.append(i)
modify = []
for i in games:
    j = ''
    for a in i:
        j += str(a)
    modify.append(j)
counts = []
for i in modify:
    cou = 0
    j = i.count('01')
    cou += j
    j = i.replace('01','')
    k = j.count('10')
    cou += k
    counts.append(cou)
print(counts)
print(dict(zip(modify,counts)))
res = []
for i in counts:
    if i % 2 == 0:
        res.append('Joe')
    else:
        res.append('John')
for i in res:
    print(i)
