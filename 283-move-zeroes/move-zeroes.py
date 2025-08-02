class Solution(object):
    def moveZeroes(self, nums):
        non_zero_=0
        for a in range(len(nums)):
            if nums[a]!=0:
                nums[non_zero_]=nums[a]
                non_zero_=non_zero_+1

        for a in range(non_zero_,len(nums)):
            nums[a]=0  

a1=[0,1,0,3,12]
sol=Solution()
sol.moveZeroes(a1)
print(a1)                 
        