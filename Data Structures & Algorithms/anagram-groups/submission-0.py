class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        result = []
        for i in range(len(strs)):
            sword = str(sorted(strs[i]))
            if sword not in hmap:
                hmap[sword] = []
            hmap[sword].append(i)
        for k,v in hmap.items():
            result.append([strs[x] for x in v])
        return result