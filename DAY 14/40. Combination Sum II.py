class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        curr=[]
        candidates.sort()
        def backtrack(start,target):
            if target ==0:
                ans.append(curr[:])
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                curr.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                curr.pop()
        backtrack(0,target)        
        return ans
