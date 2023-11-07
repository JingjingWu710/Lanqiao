n = input()
factorial = 1
count = 0
#先讨论最简单的情况，n=0
if n == "0":
    print("0")
else:
    #计算阶乘
    for i in range(1,int(n)+1):
        factorial *= i
    change = str(factorial)
    #倒过来检索有多少0
    for j in change[::-1]:
        if len(change) == "1":
            break
        else:
            if j == "0":
                count += 1
            else:
                break
    print(count)