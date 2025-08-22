<<<<<<< HEAD
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for number in range(len(nums)+1):
            result^=number
        for num in nums:
            result^=num
        return result
        

=======
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for number in range(len(nums)+1):
            result^=number
        for num in nums:
            result^=num
        return result
        

>>>>>>> f0e1976b8b4f35876b2d93ce4207bea3a3f7b037
