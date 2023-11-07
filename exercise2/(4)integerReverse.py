class Solution:
    def reverse(self, x: int) -> int:
        stringx = str(x)
        stringminorx = str(-x)
        result = 0
        if x <= 0:
            x = int(stringminorx[::-1])
            result = -x
            if abs(result) > 2147483647:
                result = 0
        elif stringx[-1] == "0":
            list(stringx).pop()
            result = int(stringx[::-1])
            if result > 2147483647:
                result = 0
        else:
            result = int(stringx[::-1])
            if result > 2147483647:
                result = 0
        return result