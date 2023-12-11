s1 = 0
s2 = 0
while s2 <= 100:
    s1 += 1
    s2 += s1
print(s1)
# 用以上代码算出最大交换次数是14，那么就是从第15个字母开始，即o，整个字符串是从o到a
# 但是多出了5，说明第5个是正确的位置，即j应该放在第一个
result = "abcdefghiklmnoj"[::-1]
print(result)



