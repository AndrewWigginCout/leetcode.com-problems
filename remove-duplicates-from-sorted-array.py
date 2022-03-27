#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution:
    def removeDuplicates(self, nums):
        nz=len(nums)
        i=0
        j=0
        while j<nz:
            if nums[j] in nums[:i]:
                j+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
        return i
