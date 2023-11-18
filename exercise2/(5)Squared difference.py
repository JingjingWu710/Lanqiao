LR = input()
L,R = LR.split()
L,R = int(L),int(R)
count = 0
# count1 = 0
# count2 = 0
# arr1 = []
# arr2 = []
# arr3 = []
# def squared(x):
#     count = 0
#     for w in range(1,x+1):
#         for l in range(w):
#             squareddif1 = pow(w,2) - pow (l,2)
#             if squareddif1 <= x+1 and squareddif1 >= 1:
#                 if squareddif1 not in arr1:
#                     arr1.append(squareddif1)
#     return len(arr1)

# for y in range(L,R+1):
#     for z in range(y):
#         squareddif2 = pow(y,2) - pow (z,2)
#         if L > 1:
#             count1 = squared(L)
#             if squareddif2 <= R and squareddif2 >= L:
#                 if squareddif2 not in arr2:
#                     arr2.append(squareddif2)
#                     count2 += 1
#         else:
#             if squareddif2 <= R and squareddif2 >= L:
#                 if squareddif2 not in arr3:
#                     arr3.append(squareddif2)
#                     count2 += 1
# print(count1)
# print(count1+count2)

# for i in range(L,R+1):
#     if i % 4 == 0 or i % 2 == 1:
#         count += 1
# print(count)
# 已知4的倍数或奇数可以是任何非负整数的平方差
# 因此只用算出两个区间里有多少4的倍数和奇数就好了
if R % 2 == 0 and L % 4 != 0:
    # 分别计算[1,R]和[1,L]的奇数和4的倍数个数
    # 需要特殊考虑L的情况，但是
    # 计算[1,L]的奇数和4的倍数缺奇数（当L是奇数，计算L//2时L本身不能被计入），R//2可以补上；
    # 所以不用添加任何东西
    count = R // 4 + R // 2 - L // 4 - L // 2
elif L % 4 == 0 and R % 2 == 0:
    count = R // 4 + R // 2 - L // 4 - L // 2 + 1
# 当区间头尾一个是4的倍数一个是奇数时，补上它们本身
else:
    count = R // 4 + R // 2 - L // 4 - L // 2 + 2
print(count)