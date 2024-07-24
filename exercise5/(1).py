# 计算数位和的函数
def digit_sum(num):
    # if num >= 10:
    #     sum = 0
    #     current = num
    #     # 累加除10，100，1000...的余数
    #     while current // 10 != 0:
    #         sum += current % 10
    #         current //= 10
    #         # 除到剩最后一个数的时候就直接加上它
    #         if current < 10:
    #             sum += current
    #     return sum
    # # 如果num小于10就直接返回它本身就好了
    # else:
    #     return num

    # 也可以转换成字符串相加
    dsum = sum(int(x) for x in str(num))
    return dsum

n = int(input())
m = int(input())
arr = [0]*1000002
# 用dif储存数位和
dif = [0]*1000002
# 导入数据至列表
for j in range(1,n+1):
    arr[j] = j
    dif[j] = digit_sum(j)
for w in range(1,n+1):
    preIndex = w - 1
    cur = arr[w]
    # 插入排序法，超时了，应该有更简单的排序，我研究研究
    while preIndex > 0 and dif[arr[preIndex]] > dif[cur]:
        arr[preIndex+1] = arr[preIndex]
        preIndex -= 1
    if dif[preIndex] == dif[cur]:
        arr[preIndex+1]= max(arr[preIndex],cur)
        arr[preIndex] = min(arr[preIndex],cur)
    else:
        arr[preIndex+1] = cur

print(arr[m])

        

