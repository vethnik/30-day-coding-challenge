class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        if s[::-1]==str(x):
            return True
        else:
            return False