class Solution(object):
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort(reverse=True)

        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0] 

a=[3,2,1]
sol=Solution()
b=sol.thirdMax(a)
print(b)            

        