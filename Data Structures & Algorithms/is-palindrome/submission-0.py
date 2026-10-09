class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(0,len(b)//2):
            if b[i]==b[-i-1]:
                continue
            else:
                return False
        return True
