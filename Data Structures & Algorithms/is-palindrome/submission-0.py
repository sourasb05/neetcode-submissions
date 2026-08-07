class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        s.join
        i = 0
        j = len(s)-1

        while i <= j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True