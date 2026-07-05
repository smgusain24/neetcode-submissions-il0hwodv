class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r, cnt = 0, 0, 0
        maxLen = 0
        d = {}
        while r<n:
            while s[r] in d:
                d.pop(s[l])
                l+=1
                cnt-=1
            
            d[s[r]]=1
            cnt+=1
            maxLen = max(maxLen, cnt)
            r+=1 
                
        return maxLen