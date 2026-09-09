class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElem = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                majElem = nums[i]
            if nums[i] == majElem:
                cnt+=1 
            else:
                cnt-=1
        return majElem
