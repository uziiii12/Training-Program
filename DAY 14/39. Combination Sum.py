class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        curr=[]
        def backtrack(start,target):
            if target==0:
                ans.append(curr[:])
                return
            if target<0 :
                return
            for i in range(start,len(candidates)) :
                curr.append(candidates[i])
                backtrack(i,target-candidates[i])
                curr.pop()
        backtrack(0,target)
        return ans              
        