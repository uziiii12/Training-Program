class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i in s:
            if i in seen :
                seen[i]+=1
            else:
                seen[i]=1
        for i in seen:
            if (seen[i]==1):
                return s.index(i)
        return -1                    