words = ['lamp','plam','eat','ate','i','i']
m_words = [''.join(sorted(i)) for i in words]
a = list(zip(words,m_words))
d = {}
for i in a:
    d.setdefault(i[1],[]).append(i[0])
res = [j for j in d.values()]
print(res)