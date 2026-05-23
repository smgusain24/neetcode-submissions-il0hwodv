class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        while left<=right:
            ssum = nums[left]+nums[right]
            if ssum ==target:
                return [left+1, right+1]
            elif ssum >target:
                right-=1
            else:
                left+=1
            