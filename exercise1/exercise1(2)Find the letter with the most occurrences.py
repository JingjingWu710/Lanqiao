import os
import sys
words = input()
index = 1
count1 = 0
count2 = 0
list = []
while len(words) <= 1000 and index < len(words):
      # 遍历所有字母，检查前后是否有与其相同的字母，并计数，
      # 每一次while循环清空count1，留下较大的数字count2
      for i in words[:index] and words[index:]:
            if i == words[index]:
              count1 += 1
      if count1 >= count2:
        count2 = count1
        wordstmp = words[index]
      count1 = 0
      index += 1
#参考了别人的，之前不认识count函数。
#想过用dic解决，有思路，但太久没用dic忘记语法是什么了……
for j in words:
    if words.count(j) == count2:
        list.append(j)
list.sort()
print(list[0])
print(count2)
 #在系统检测有一个测试用例段错误，没找出原因

 # 找到了用dics解决的答案，记录一下，让我重新复习了dics，
 # 还让我对sorted函数的运用有了更深的了解
# word = input()
# dicts = {}
# for i in word:
#     dicts[i] = dicts.get(i,0) + 1（i出现一次，value就加1）
# l = sorted(dicts.items(), key = lambda x:[x[1],-ord(x[0])])   用key指定两个排序标准，
# 主要标准是x[1]也就是每一组的第二个元素value，次要标准是ord(x[0])也就是字母序，
# 添加负号代表降序
# print(l[-1][0])
# print(l[-1][1])