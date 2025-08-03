class Solution(object):
    def removeElement(self, nums, val):
         b=0
         for a in range(len(nums)):
            if nums[a]!=val:
             nums[b]=nums[a]
             b=b+1
         return b  

y=[3,2,2,3]
sol=Solution()
sol.removeElement(y,3)
print(y)

        