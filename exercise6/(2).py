n,k = map(int,input().split())
a = input().split()
l = []
for i in a:
    l.append(int(i))

l = [0] + l
ans = 1
dp = [0]*(n+1)
dp[1] = 1
# for i in range(2,n+1):
#     max_len = 0
#     for j in range(1,i):
#         # 在这个范围内遍历，dp[i]表达i之前包括i有多长的递增子序列
#         # 找出局部最长的子序列，最终成为dp[i]
#         if l[i] >= l[j] and dp[j] > max_len:
#             max_len = dp[j]
            
#     # dp[i]不一定是最终的最长子序列
#     dp[i] = max_len + 1
#     # print(max_len,dp[i])

# dp2 = [0] * (n + 1)
# for i in range(1,n+1):
#     max_len2 = 0
#     if i + k > n:
#         break
#     if max(l[i+k,n]) >= l[i-1]:
#         for j in range(i+k,n+1):
#             if l[j] >= l[i]:
#                 if dp[j] > max_len2:
#                     max_len2 = dp[j]
#     dp2[i] = dp[i-1] + k + max_len2



# print(dp,ans)
# print(ans,dp,l)

# 这个思路是算出每个子串有多少个不符合上升的元素，
# 用k补齐，可惜系统没给我答案正确，呵呵，我用题目给的用例是对的
for i in range(1,n):
    count = 0
    tmp = i-1
    for j in range(i-1,-1,-1):
        if l[i] >= l[j]:
            if l[j] <= l[tmp]:
                dp[i] += 1
            else:
                count += 1
        else:
            count += 1
        tmp = j
        # print(l[j],dp[i])
    if count >= k:
        dp[i] += k
    else:
        dp[i] += count
    # print(dp)        
print(max(dp))
l += [0]

# for i in range(n):
#     if l[i] >= l[i-1]:
#         dp1[i] = dp1[i-1] + 1
#     else:
#         dp1[i] = 1

# for i in range(n): 
#     for j in range(i+k+1,n):
#         if j > n - 1:
#             break
#         if l[j] >= l[i] and j == i+k+1:
#             dp[i] += 1
#             continue
#         elif l[j] < l[i] and j == i+k+1:
#             break
#         if l[j] >= l[j-1]:
#             dp[i] += 1
#         else:
#             break

# dp3 = []

# for i in range(n):
#     dp3.append(dp1[i]+dp[i])
# print(dp1)
# print(dp)
# print(dp3)
# print(max(dp3)-1+k)

     
        

        # if j - k >= 0:
        #     if l[j-1] <= l[j]:
        #         dp[j] = dp[j-1] + 1
        #     else:
        #         if l[j] >= l[]
        #         dp[j] = max(dp[j-k]
# l.append(0)

# def find(a,b,dp,dp):
#     for j in range(a,b):
#         if l[j] >= l[j-1]:
#             dp[j] = dp[j-1] + 1
#         else:
#             dp[j] = 1
#         dp[dp[j]] += 1
#     max_arr = max(1,max(dp))
#     return [max_arr,dp[max_arr],dp,dp]

# b = find(0,n,[0]*(n+1),[0]*(n+1))
# max_arr,num_max,dp,dp = a[0],a[1],a[2],a[3]
# for i in range(num_max,0,-1):

# for i in range(dp[max_arr]):
#     dp[dp.index(max_arr)] += k
#     dp[dp.index(max_arr)+k] += k
#     if dp.index(max_arr)+k+1 < len(l) and dp[dp.index(max_arr)] <= dp[dp.index(max_arr)+k+1]:
#         dp[dp.index(max_arr)+k+1] = 