class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap = {}

        for num in nums1:
            hashmap[num] = 1

        result = []

        for num in nums2:

            if num in hashmap:
                result.append(num)
                del hashmap[num]

        return result