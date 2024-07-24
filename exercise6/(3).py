# 用最大公约数求最小公倍数
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
 
def lcm(a,b):
    return a * b // gcd(a,b)

# 建立动态列表实时更新从i到j的最短间距，并加上从起始点到i的最短间距
# 把每个元素先设置成无穷大，这样就会在第一次遍历到某个数的时候总是取lcm(i,j)+res[i]了
res = [float('inf')] * 2022
res[1] = 0
for i in range(1,2022):
    for j in range(i+1,i+22):
        if j > 2021:
            break
        res[j] = min(res[j],lcm(i,j)+res[i])

print(res[2021])
