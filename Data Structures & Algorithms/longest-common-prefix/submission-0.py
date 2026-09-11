class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        result = ""
        for i in range(len(min(first,last))):
            if first[i]!=last[i]:
                break
            result+=first[i]
        return result
            
