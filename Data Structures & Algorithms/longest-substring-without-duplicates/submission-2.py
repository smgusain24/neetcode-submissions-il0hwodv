class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r= 0, 0
        maxLen = 0
        d = {}
        while r<n:
            if s[r] in d:
                l = max(l, d[s[r]]+1)
            
            d[s[r]]=r
            maxLen = max(maxLen, r-l+1)
            r+=1 
                
        return maxLen