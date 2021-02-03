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
for i,j in d.items():
    



# main = []
# gift = 0
# for i,j in new_d.items():
#     gift += len(j) * j[0]
#     gifts = [((j[i] - j[i-1]) * (len(j) - i)) + gift for i in range(len(j)) if i < factor]
#     main.append(gifts)
# print(main)