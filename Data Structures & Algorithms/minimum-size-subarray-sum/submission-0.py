class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        min_length = float("inf")
        for i in range(len(nums)):
            high += nums[i]
            while high >= target:
                min_length = min(min_length, i - low + 1)
                high -= nums[low]
                low +=1
        if min_length == float("inf"):
            return 0
        return min_length
        