class Solution(object):
    def containsDuplicate(self, nums):
        hashset=set()
        for a in nums:
            if a in hashset:
                return True
            hashset.add(a)
        return False        