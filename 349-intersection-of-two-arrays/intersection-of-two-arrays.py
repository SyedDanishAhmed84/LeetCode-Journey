class Solution(object):
    def intersection(self, nums1, nums2):
       set1=set(nums1)
       set2=set(nums2)

       return list(set1 & set2)

a=[1,2,2,1]
b=[2,2]
sol=Solution()
c=sol.intersection(a,b)
print(c)

    