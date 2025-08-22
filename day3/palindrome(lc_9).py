<<<<<<< HEAD
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
=======
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
>>>>>>> f0e1976b8b4f35876b2d93ce4207bea3a3f7b037
            return False