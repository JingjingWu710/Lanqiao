class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 这题很简单，虽然有好几行数组，但我们归根结底只是在每一行里做二分查找
        # 而且每一行第一个数大于上一行最后一个数这个条件给了我们很大便利
        # 我们可以先拿每一行的最后一个数和target比较
        # 这样可以很快确定target可能在哪一行
        l = 0
        r = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] > target:
                # 某行最右边一个数大于target意味着这一行可能存在target
                # 于是在这一行二分法查找target
                while l <= r:
                    m = (l + r) // 2
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                pass
        return False   