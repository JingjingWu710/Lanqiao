class Solution:
    def integerBreak(self, n: int) -> int:
        result = 1
        #算了算发现所有大于等于5的数都拆成3×3×3...×3×4
        # 或3×3×3...×3×2乘积最大
        if n >3:
            if n % 3 == 0:
                #能被3整除的全部拆成3
                for i in range(1,n//3+1):
                    result *= 3
            elif n % 3 == 1:
                #余1的最后是3×4，因为它比3×3×1大
                for j in range(1,n//3):
                    result *= 3
                result *= 4
            else:
                for w in range(1,n//3+1):
                #余2的最后是3×2
                    result *= 3
                result *= 2
            return result
        elif n == 3:
            #下面两个判断语句是为了通过n = 3和n = 2的情况
            return 2
        else:
            return result