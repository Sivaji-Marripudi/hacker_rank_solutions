num = int(input('enter number : '))
l = []
prime_number = 0
if num > 1 and num != 4:
    for i in range(2,num//2):
        if num % i == 0:
            break
    else:
        for i in str(num):
            j = int(i)
            l.append(j)
print(l)
