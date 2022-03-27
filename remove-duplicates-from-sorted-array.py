'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

Runtime: 172 ms, faster than 25.14% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 67.31% of Python3 online submissions for Remove Duplicates from Sorted Array.
Next challenges: 
'''
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
