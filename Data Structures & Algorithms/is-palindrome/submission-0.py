class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = ""
        for ch in s:
            if ch.isalnum():
                q+=ch


        l,r = 0, len(q)-1
        print(q)
        while l<=r:
            if q[l].lower()!=q[r].lower():
                return False
            l+=1
            r-=1
        return True