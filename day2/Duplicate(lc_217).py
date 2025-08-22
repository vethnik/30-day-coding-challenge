<<<<<<< HEAD
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
=======
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
>>>>>>> f0e1976b8b4f35876b2d93ce4207bea3a3f7b037
        return len(nums) != len(set(nums))