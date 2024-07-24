# import itertools
n,k = map(int,input().split())
a = [int(i) for i in input().split()]
s = [int(i) for i in input()]
ind = []
num = []
for index, item in enumerate(s):
    if item == 1:
        ind.append(index)
for i in ind:
    num.append(a[i])

def judge(dp,replace):
    for i in reversed(dp):
        if i > replace:
            return i
dp = []
count = 0
dp.append(a[0])
for i in range(1,len(a)):
    k_num = 0
    if a[i] >= dp[-1]:
        dp.append(a[i])
        if i in ind:
            k_num += 1
    if k_num >= k:
        count += 1
# 试图求出每一种可能并一个个排除。。已放弃！
# p = []
# for i in range(k,len(ind)+1):
#     p = p.append(list(itertools.permutations(num,i)))

# for i in range(1,len(ind)):
#     if ind[i] <= 

