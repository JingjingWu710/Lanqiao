
# while sentence:
#     for word in sentence:
#         for vcb in dictionary:
#             if vcb in words:
#                 count = len(words) - len(vcb)
#                 sentence = sentence[len(sentence)-len(words):len(sentence)]
#                 words = ""
#                 break
#             else:
#                 pass
#         words += word

# def respace():
#     count = 0
#     dictionary = input().split()
#     sentence = input()
#     min_word = len(min(dictionary,key=len))
#     max_len = 0
#     if len(sentence) < min_word:
#         return sentence
#     for i in range(1,len(sentence)): 
#         for j in range(i-1,-1,-1):
#             if i - j < min_word:
#                 pass
#             else:
#                 if sentence[j:i+1] not in dictionary:
#                     pass
#                 else:
#                     if max_len <= i - j:
#                         max_len = i - j
#         count += max_len
#         max_len = 0
#     return(len(sentence)-count)

# def unrecognized_characters(dictionary, sentence):
#     n = len(sentence)
#     # dp[i]表示前i个字符中未识别的字符数
#     dp = [0] + [float('inf')] * n  # 初始化dp数组

#     for i in range(1, n + 1):
#         for word in dictionary:
#             # 尝试将当前位置向前移动，看是否能匹配到词典中的单词
#             if i >= len(word) and sentence[i - len(word):i] == word:
#                 dp[i] = min(dp[i], dp[i - len(word)])

#         # 在当前位置插入空格，使得未识别的字符数加一
#         dp[i] = min(dp[i], dp[i - 1] + 1)

#         # 打印dp数组变化过程
#         print(f"dp[{i}] = {dp[i]}")

#     return dp[n]

def respace():
    dictionary = input().split()
    sentence = input()
    # 如果sentence或dic是空集的话
    if len(sentence) == 0:
        return 0
    if len(dictionary) == 0:
        return len(sentence)
    # 用动态列表dp更新最小未识别的字符数
    # 多一个0是为了在dp[0] = dp[0-1] + 1时有数参考
    dp = [0] * (len(sentence)+1)
    # i从0开始方便用dp[i]对应从sentence[0]直至sentence[i]有几个未识别的字符，
    # 还可以直接索引到sentence遍历到的字符
    for i in range(len(sentence)):
        dp[i] = dp[i-1] + 1
        for word in dictionary:
            # sentence[i-len(word)+1:i+1]的start要+1是因为要包括word第一个字母
            # 直接减len(word)不+1，sentence[i-len(word)]是直接索引到word前一个字符的
            # 那这个片段就会多一个字符了
            if i + 1 >= len(word) and sentence[i-len(word)+1:i+1] == word:
                # 如果一个字符串里包含两个字典单词，如brother，包含brother和her
                # 就要分别对比减去哪个单词所剩的未识别字符少
                dp[i] = min(dp[i - len(word)],dp[i])
    # 返回dp的倒数第二个数，因为最后一个始终是0
    return dp[-2]

print(respace())

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if len(sentence) <= 0: return 0
        if len(dictionary) <= 0: return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]

# # 示例
# dictionary = ["looked", "just", "like", "her", "brother"]
# sentence = "jesslookedjustliketimherbrother"
# result = unrecognized_characters(dictionary, sentence)
# print(result)


# words = ""
# for i in sentence:
#     words += i
#     if len(words) >= min_word:
#         for k in dictionary:
#             if k not in words:
#                 pass
#             else:
#                 count += len(k)
#                 print(k,count)
#                 words = ""
#                 break

# print(len(sentence)-count)

        # if len(words) >= min_word:
        #     for k in dictionary:
        #         if k in words:
        #             words = sentence[i]
        #             count += len(k)
        #             break
        # if words == sentence[i]:
        #     break
        # words = sentence[j] + words
