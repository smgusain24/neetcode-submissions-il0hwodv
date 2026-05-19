class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        mini = float("inf")
        while left<=right:
            mid = left + (right-left)//2
            mini = min(mini, nums[mid])
            if nums[left]<nums[right]:
                if nums[left]<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[right]<=nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return mini