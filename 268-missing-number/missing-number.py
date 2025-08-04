class Solution(object):
    def missingNumber(self, nums):
       a=len(nums)
       expected_sum=a*(a+1)//2
       actual_sum=sum(nums)
       return expected_sum-actual_sum

x=[3,0,1]
sol=Solution()
sol.missingNumber(x)
print(x)       
        