# 解法二，二分查找法
N,K = map(int,input().split())
HW_list = []
while N > 0:
    HW_list.append(list(map(int,input().split())))
    N -= 1
# 题目给的最大值是100000，所以r设定为100001
l,r = 1, 100001
# 因为要得出最大边长，所以应该指针在右边时num<K，在左边时num>=K，所以循环终止条件是l<r
while l < r:
    mid = (l+r) // 2
    num = 0
    for i in range(len(HW_list)):
        num += (HW_list[i][0]//mid) * (HW_list[i][1]//mid)
    if num < K:
        r = mid
    else:
        l = mid + 1
print(l-1)
# # 解法一，暴力法，一个个试边长
# N,K = map(int,input().split())
# HW_list = []
# ccl_len = 1
# while N > 0:
#     HW_list.append(list(map(int,input().split())))
#     N -= 1
# while True:
#     num = 0
# # 用for循环分别计算N块巧克力各自能切多少块正方形巧克力
#     for i in range(len(HW_list)):
# # 我摊牌了，我不懂如何计算在长方形里能截几个正方形，所以偷偷看了答案T_T
#         num += (HW_list[i][0]//ccl_len) * (HW_list[i][1]//ccl_len)
#     if num < K:
#         break
#     else:
#         ccl_len += 1
# # 因为如果下一个边长使得num < K，那前面肯定多加了1，所以最后输出边长-1
# print(ccl_len-1)
# # 通过75%，剩下的超时了