class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            required=target-nums[i]
            if required in map:
                return[map[required],i]
            map[nums[i]]=i
        return[-1,-1]        
        