# # 解法二，我觉得这个解法能完全覆盖所有情况，时间超限了！！
# N = int(input())
# exercise = input().split()
# number = []
# exercise = list(map(int,exercise))
# # 给每个数标上序号，之后还原原来的顺序可以用
# for j in range(len(exercise)):
#     number.append([j,exercise[j]])
# # 以刷题数排序
# number.sort(key=lambda x:x[1])
# mid = number[(len(exercise))//2][1]
# result = []
# for z in range(len(exercise)):
#     # 如果只有一个人就不用对比了，直接输出0
#     if len(exercise) == 1:
#         result.append([number[z][0],0])
#         break
#     # 如果是6 10 12 15 20或6 10 12 12 15这样的，12就是中位数，遍历到中位数和中位数右边的数不需要任何改动
#     elif mid != number[len(exercise)//2-1][1]:
#         if z < mid:
#             result.append([number[z][0],mid-number[z][1]+1])
#         else:
#             result.append([number[z][0],0])
    
#     # 如果是6 12 12 15 20这样的，则中位数和中位数前的数都要改变
#     elif number[len(exercise)//2-1][1] == mid and number[len(exercise)//2+1][1] != mid:
#         if z <= mid:
#             result.append([number[z][0],mid-number[z][1]+1])
#         else:
#             result.append([number[z][0],0])
#     # 如果是6 12 12 12 15这样的，中位数前后的数都和中位数一样则中间相同的数都不需要改变，加个min以防全部数字都是一样的
#     elif mid == number[len(exercise)//2+1][1] == number[len(exercise)//2-1][1] and min(exercise) != number[z][1]:
#         if number[z][1] >= mid:
#             result.append([number[z][0],0])
#         else:
#             result.append([number[z][0],mid-number[z][1]+1])
#     else:
#     # 这是所有数字都一样的情况
#         result.append([number[z][0],mid-number[z][1] +  1])
        

# result.sort()
# result2 = []
# for y in range(len(result)):
#     result2.append(result[y][1])
# print(" ".join(str(w) for w in result2))

# # 解法一，正确率60%
# N = int(input())
# exercise = input().split()
# exercise_list = []
# number = []
# for i in exercise:
#     i = int(i)
#     exercise_list.append(i)
# mid = (len(exercise_list)) // 2
# for j in range(len(exercise_list)):
#     number.append([j,exercise_list[j]])
# number.sort(key=lambda x:x[1])
# result = []
# for z in range(len(exercise_list)):
#     if len(exercise_list) == 1:
#         result.append([number[z][0],0])
#         break
#     elif z == mid and (mid != number[mid-1][1] and mid != number[mid+1][1]):
#         result.append([number[z][0],0])
#     elif z == mid:
#         result.append([number[mid][0],mid - number[z][1] +  1])
#     elif number[z][1] - mid <= 0:
#         result.append([number[z][0],mid - number[z][1] +  1])
#     else:
#         result.append([number[z][0],0])
        

# result.sort()
# result2 = []
# for y in range(len(result)):
#     result2.append(result[y][1])
# print(" ".join(str(w) for w in result2))

N = int(input())
exercise = input().split()
number = []
exercise = list(map(int,exercise))
# 给每个数标上序号，之后还原原来的顺序可以用
for j in range(len(exercise)):
    number.append([j,exercise[j]])
# 以刷题数排序
number.sort(key=lambda x:x[1])
mid = number[(len(exercise))//2][1]
result = []
for w in range(len(number)):
    # 只有一个同学的时候
    if len(number) == 1:
        result.append([number[w][0],0])
        break
    # 这个同学刷题数量大于中位数
    if number[w][1] > mid:
        result.append([number[w][0],0])
    # 等于中位数的时候需要分类讨论，存在所有数都一样的可能
    elif number[w][1] == min(exercise) == max(exercise):
        result.append([number[w][0],1])
    # 遍历到的数等于中位数的情况，可能是中位数自己，可能是中位数之前或之后的数
    elif number[w][1] == mid:
        # 遍历中位数左边和中位数相等的数：
        if w < len(number) // 2:
            result.append([number[w][0],1])
        # 如果只是单纯遍历到中位数，且中位数左边没有和它相等的数时：
        elif w == len(number) // 2 and mid != number[w-1][1]:
            result.append([number[w][0],0])
        # 如果中位数之前就有和中位数相等的数，又是新的情况，中位数也要变：
        elif w == len(number) // 2:
            result.append([number[w][0],1])
        # 虽然它和中位数相等，但已经在中位数右边了，那什么都不用做
        else:
            result.append([number[w][0],0])
    else:
        result.append([number[w][0],mid-number[w][1]+1])
result.sort()
result2 = []
for y in range(len(result)):
    result2.append(result[y][1])
print(" ".join(str(w) for w in result2))
