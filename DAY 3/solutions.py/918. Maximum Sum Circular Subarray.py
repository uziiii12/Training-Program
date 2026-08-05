class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        curMax = maxSum = nums[0]
        curMin = minSum = nums[0]

        for i in range(1, len(nums)):

            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)

            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)