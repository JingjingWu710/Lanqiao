s = [1,1,1]
count = 3
while count < 20190324:
    #当一个数很大的时候，可以不用管更高位数的进位
    #因为要后四位，所以除10000求余数就好了
    new_num = (s[0] + s[1] + s[2])%100000
    s.append(new_num)
    count += 1
    del s[0]

stringnum = str(s[-1])
print(stringnum[-4:])