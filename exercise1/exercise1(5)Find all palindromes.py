#class Solution:
def countSubstrings(s: str) -> int:
        #和前面寻找最长回文思路几乎一模一样，只不过这一题一找到回文就记一次数
        #还有不用记最大数，且初始值是字符串的长度，因为每一个字母就是一个回文
        count = len(s)
        dp = [[False for _ in range(len(s))]for _ in range(len(s))]
        for i in range(1,len(s)):
            for j in range(i):
                if i - j <= 2:
                    if s[i] == s[j]:
                        count += 1
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i-1][j+1]:
                        count += 1
                        dp[i][j] =True
        return count

s = "aaa"
print(countSubstrings(s))
