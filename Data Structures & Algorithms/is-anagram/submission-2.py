class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d = {}
        for l in s:
            d[l] = d.get(l,0)+1
        for l in t:
            if l not in d:
                return False
            d[l]-=1
            if d[l] == 0:
                del d[l]
        return True