m,n = map(int,input().split())
k = int(input())
result = m * n
# 为啥答案要写range(m*n)，比如有20株植物，遇到x=20的时候
# s[20]已经出界了啊
arr = list(range(m*n+1))

# 找根节点的循环函数
# 顺便把沿路对应的arr[x]都改成根节点

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]
# 根不一样的就使j端和i端有一样的根
# 同时减掉1，因为j已经没有自己的根了
def merge(i,j):
    i = find(i)
    j = find(j)
    if i == j:
        return False
    arr[j] = i
    return True

for _ in range(k):
    i,j = map(int,input().split())
    if merge(i,j):
        result -= 1

print(result)