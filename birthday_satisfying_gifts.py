test_cases = int(input('enter the testcases : '))
frnds_list = [int(input()) for i in range(test_cases)]
num_of_frnds = []
for i in frnds_list:
    a = [int(input('frnds : ')) for j in range(i) ]
    num_of_frnds.append(a)
print(num_of_frnds)
satisfy = [int(input('factors : ')) for i in range(test_cases)]
d = dict(zip(satisfy,num_of_frnds))
print(d)
