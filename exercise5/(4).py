import itertools
dig = "abcdefg"

dic = {"a":["f","b"],"b":["a","g","c"],"c":["b","g","d"],
       "d":["c","e"],"e":["f","g","d"],"f":["a","g","e"],
       "g":["f","b","e","c"]}
# 我的思路就是把abcdefg的所有可能排序都列举出来，再一个个排除不相通的
# 手算很容易，但是写代码很困难，感觉可以用并查集，
# 但是手动列举好难，于是我学会了combinations函数

seq = []
result = 0
for i in range(1,8):
    # 把所有可能的组合列出来
    all_possibility = list(itertools.permutations(dig,i))
    # 遍历元组，把元组里的元素合并
    for j in all_possibility:
        seq.append("".join(j))

for i in range(1,len(seq)):
    count = 0
    for j in range(1,len(seq[i])-1):
        # 一个个遍历每一个可能，查每个字母左右两边有没有和自己相连
        if seq[i][j-1] in dic[seq[i][j]] and seq[i][j+1] in dic[seq[i][j]]:
            count += 1
        else:

            #如果有一个地方不连在一起就结束遍历（但是我要考虑到有些排序可能不按顺序排，
            # 但仍然连在一起，这样就不好查询，如abfc，b和f不相连，但图上是连的，感觉可以用并查集，但是想不出来！！
            # 目前网上没有一个答案是我能看懂的orz
            break
    if count == len(seq[i]) // 2:
        result += 1
print(result)