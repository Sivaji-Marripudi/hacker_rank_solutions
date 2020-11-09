'''
Assignment: Find who tweeted the most

You will be given a list of tweets
Your program should find the user who has tweeted the most

Note:
If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
Use Python 3
Follow python coding style guide
Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

Input format:
Read the input from console.
First line of input should be number of test cases
Remaining lines of input should contain each test case input. 

For each test case input:
First line should contain number of tweets.
Followed by N lines, each containing user name and tweet id separated by a space.

Output format:
Find the user with max number of tweets. Print user name and total number of tweets.


Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3


Sample 2:
Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output
kohli 2
sachin 2
sehwag 2


Sample 3:
Input 
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

Output
sachin 2
sehwag 2
dhoni 4

Sample 4:
Input
3
4
sehwag tweet_id_2
sehwag tweet_id_4
sachin tweet_id_1
sachin tweet_id_3
7
sehwag tweet_id_10
sehwag tweet_id_11
kohli tweet_id_12
sachin tweet_id_13
sachin tweet_id_14
sachin tweet_id_1
sehwag tweet_id_4
5
sachin tweet_id_2
kohli tweet_id_4
kohli tweet_id_1
kohli tweet_id_3
sachin tweet_id_5

Output:
sachin 2
sehwag 2
sachin 3
sehwag 3
kohli 3
'''
test_cases = int(input())
main = []
for i in range(test_cases):
    j = int(input())
    l = []
    for i in range(j):
        j = input('enter names : ')
        l.append(j)
    main.append(l)
main1 = []
for i in main:
    c = []
    for j in i:
        a = j.split()
        b = a[0]
        c.append(b)
    main1.append(c)
res = []
from collections import Counter
for i in main1:
    j = Counter(i)
    res.append(j)
res1 = []
for i in res:
    max_value = max(i.values(),key = (lambda j:i[j]))
    d = {a:b for a,b in i.items() if b == max_value}
    res1.append(d)
res2 = []
import operator
for i in res1:
    j = sorted(i.items(),key = operator.itemgetter(0))
    res2.append(j)
for i in res2:
    for a in i:
        print('{}  {}'.format(a[0],a[1]))