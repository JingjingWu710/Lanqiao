def isValid(s: str) -> bool:
# s = input()
# list = []
# count = 0
# for j in s:
#     list.append(j)
# for i in list[::2]:
#     if i == "(":
#         if s[s.index(i)+1] == ")":
#             count += 1
#             pass
#         else:
#             result = False
#             print(result)#return False
#             break
#     elif i == "[":
#         if s[s.index(i)+1] == "]":
#             count += 1
#             pass
#         else:
#             result = False
#             print(result)#return False
#             break
#     elif i == "{":
#         if s[s.index(i)+1] == "}":
#             count += 1
#             pass
#         else:
#             result = False
#             print(result)#return False
#             break
#     else:
#         print("False")
#         break
#     if count == len(s)//2:
#         print("True")
   #我自己想出来的不用字典的方法，不知道为什么leetcode上通不过的测试用例在我的编译器上可以通过

        dic = {")":"(","]":"[","}":"{"}
        arr = []
        for i in s:
            if i in dic.values():
                arr.append(i)
            if i in dic.keys():
                if arr == []:
                    return False
                if dic[i] == arr[-1]:
                    #print(arr)
                    arr.pop()
                else:
                    return False

        if arr == []:
            return True
        else:
            return False

#为什么测试用例"([)]"答案错误……明明符合题目条件，应该是True才对
#直接移掉和右括号配对的左括号，不知道为什么参考答案会用pop，
# 列表最后一个元素不一定是和右括号一样类型的左括号啊，
# 如 "({{{{}}}))"，消掉中间所有正确闭合的{}后，剩下({))。。。
# 写到这里突然醒悟，直接判断第一个右括号的value和列表最后一个元素是不是相等就好了，
# 因为嵌套在其它括号里的括号要完整闭合，所以第一个右括号和最后一个左括号一定是一对
# （这一段是在我最后搞懂题目的意思写的）