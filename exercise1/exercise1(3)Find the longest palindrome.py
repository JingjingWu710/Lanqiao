class Solution:
    def longestPalindrome(self, s: str) -> str:
        #搜到了两个办法，看了之后努力自己又写了一遍并写下自己的理解
        #第一个方法
        lgpld = ""#储存最长字符串
        for i in s:
           #设置beginning不断往i的前面查找，
           #减去len(lgpld)是因为要找到比目前储存的回文更长的回文
           #再减去1是为了当i和len(lgpld)相等，使字符串往左移到更前的位置
           beginning = max(i-len(lgpld)-1,0)
           tem = s[beginning:i]
           #[::-1]是倒序切片，将字符串倒过来逐个检查与原字符串是否相同
           if tem == tem[::-1]:
               lgpld = tem
           else:
               #去掉第一个字母，再检测是否回文
               tem = tem[1:]
               if tem == tem[::-1]:
                   lgpld = tem
        return lgpld

        #第二个方法，建立二维布尔数组
        length = len(s)
        max_len = 1 #最大长度初始值为1，因为每一个字符串至少都会有一个字母组成的回文
        if length == 1:
            return s
        else:
            dp = [[False for _ in range(length) for _ in range(length)]]#建立一个length×length的表，用来记录不同情况的回文
            for end in range(1,length):
                #end控制子串的右边（或结束处），例如，当end=2时，start需要遍历0、1；
                #当end=3时，start就被控制在0、1、2之间。
                for start in range(end):
                    #简化长度小于等于2的子串处理（其实不用它也可以）
                    if end - start <= 2:
                        if s[start] == s[end]:
                            dp[start][end] = True#表格dp[end][start]这一格记录为True
                            pldlen = end - start + 1
                    else:
                        #头尾相同，中间是回文，代表包括头尾的子串也是回文
                        if s[start] == s[end] and dp[start+1][end-1]:
                            dp[start][end] = True
                            pldlen = end - start + 1
                    #替换最长回文数，更新回文起点
                    if pldlen > max_len:
                        max_len = pldlen
                        max_len_start = start

        return s[max_len_start:max_len_start+max_len]