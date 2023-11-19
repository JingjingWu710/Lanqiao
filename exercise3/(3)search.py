nums = [4,5,6,7,8,0,1,2]
target = 0
l = 0
r = len(nums) - 1
def search(nums,target):
    # 解法二，考点是二分查找，用二分查找解题
    if target not in nums:
        return -1
    while l <= r:
        # 这道题比大小不管用了，所以就判断左右边有没有target就好了
        mid =(l+r)//2
        if nums[mid] == target:
            return mid
        elif target in nums[l:mid]:
            r=mid - 1
        else:
            l=mid + 1
#解法一，有函数不用是笨蛋B-)
        # if target not in nums:
        #     return -1
        # else:
        #     return nums.index(target)

        