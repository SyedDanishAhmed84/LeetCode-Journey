class Solution(object):
    def removeDuplicates(self, nums):
       if not nums:
        return 0

       a=0

       for b in range(1,len(nums)):
        if(nums[b]!=nums[a]):
            a=a+1
            nums[a]=nums[b]

       return a+1        

x=[1,1,2]
sol=Solution()
sol.removeDuplicates(x)
print(x)
