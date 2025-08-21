class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_lists=[]
        nums_lists=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zero_lists.append(nums[i])
            else:
                nums_lists.append(nums[i])
        
        nums[:]=nums_lists+zero_lists
