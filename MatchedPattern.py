qu = ['FooBar','FooBarTest','FootBall','FrameBuffer','ForceFeedBack']
patt = 'FB'
m_qu = []
for i in qu:
    s = ''
    for j in i:
        if j.isupper():
            s += ' ' + j
        else:
            s += j
    m_qu.append(s)
m1_qu = [i.split() for i in m_qu]
m2_qu = []
for i in m1_qu:
    m_pattern = ''
    for j in i:
        m_pattern += j[0]
    m2_qu.append(m_pattern)
res = []
for i in m2_qu:
    if i == patt:
        res.append(True)
    else:
        res.append(False)
print(res)
