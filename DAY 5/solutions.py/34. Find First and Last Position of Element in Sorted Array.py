class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    def findFirst(self, nums, target):

        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                answer = mid
                right = mid - 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return answer

    def findLast(self, nums, target):

        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                answer = mid
                left = mid + 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return answer