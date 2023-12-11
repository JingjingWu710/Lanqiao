# 这道题就是要让大的数尽可能往交叉区间靠
# 算交叉区间就要用前缀和
n = int(input())
a = [0]*1000001
section = [0]*1000001
section_sum = [0]*1000001
# 因为题目描述的“第L”“第R”和列表下标不一样，先把它往后挪一个元素
a[1:n+1] = map(int,input().split())
m = int(input())
for _ in range(m):
    # 输入区间
    l, r = map(int,input().split())
    # 标注区间，这样算前缀和时就知道哪里区间结束了，一正一负是为了区分左括号和右括号
    section[l] += 1
    section[r+1] -= 1
# 算区间前缀和，如果section_sum[i] == 0，意味着a[i]不在任何区间范围内
# 如果 == 1，说明它在一个区间内；如果 == 2，说明它在两个区间的交叉范围内，以此类推
for i in range(1,n+1):
    section_sum[i] = section_sum[i-1] + section[i]
result1 = 0
result2 = 0
# 算原区间和
for i in range(1,n+1):
    result1 += a[i] * section_sum[i]
# 越大的数在越多交叉区间的范围内越好，用sort使a的大数和重合多的交叉区间对齐
a = sorted(a,reverse=True)
section_sum = sorted(section_sum,reverse=True)
# 算排序后的区间和
for i in range(n):
    result2 += a[i] * section_sum[i]

print(result2-result1)