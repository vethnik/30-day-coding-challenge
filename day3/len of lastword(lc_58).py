<<<<<<< HEAD
class Solution:
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        
        if not words:
            return 0
        
=======
class Solution:
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        
        if not words:
            return 0
        
>>>>>>> f0e1976b8b4f35876b2d93ce4207bea3a3f7b037
        return len(words[-1])