def countBits(n):
    res = []
    for i in range(n+1):
        if i % 2 == 0:
            binary = bin(i)
            string = binary[2:]
            res.append(sum(int(j) for j in string))
        else:
            res.append(res[i-1]+1)
    return res

print(countBits(5))
    