#设置一个可以灵活输入任何字母的入口，按照题目要求可要可不要
# words = input()
#sorted排列字母顺序
# words = "WHERETHEREISAWILLTHEREISAWAY"
# sortedresult = sorted(words)
#join让列表变成题目所需的字符串
# result = "".join(sortedresult)
# print(result)
#搜索学到了一个将字母转换为数字再进行排序的思路
# words = "WHERETHEREISAWILLTHEREISAWAY"
# #建立一个存放数字的列表
# numlist = []
# for i in words:
#     #将字母转换成数字
#     wordsnum = ord(i)
#     numlist.append(wordsnum)
# #将数字排序
# sortedlist = []
# while numlist != []:
#     sortedlist.append(min(numlist))
#     numlist.remove(min(numlist))
# result = "".join(chr(i) for i in sortedlist)
# print(result)
print("AAAEEEEEEHHHIIILLRRRSSTTWWWY")