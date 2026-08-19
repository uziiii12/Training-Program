class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        left = 0
        sum = 0
        answer = 0
        seen = {}

        for right in range(len(nums)):

            sum += nums[right]

            if nums[right] in seen:
                seen[nums[right]] += 1
            else:
                seen[nums[right]] = 1

            if right - left + 1 == k:

                if len(seen) == k:
                    answer = max(answer, sum)

                seen[nums[left]] -= 1
                sum -= nums[left]

                if seen[nums[left]] == 0:
                    del seen[nums[left]]

                left += 1

        return answer