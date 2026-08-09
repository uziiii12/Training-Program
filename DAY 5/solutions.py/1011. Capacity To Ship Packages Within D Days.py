class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:

            capacity = (left + right) // 2

            currentWeight = 0
            requiredDays = 1

            for weight in weights:

                if currentWeight + weight > capacity:
                    requiredDays += 1
                    currentWeight = 0

                currentWeight += weight

            if requiredDays <= days:
                right = capacity
            else:
                left = capacity + 1

        return left