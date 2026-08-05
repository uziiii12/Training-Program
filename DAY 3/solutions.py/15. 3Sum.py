class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                sum=nums[i]+nums[L]+nums[R]
                if sum==0:
                    result.append([nums[i],nums[L],nums[R]])
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                    while L<R and nums[R]==nums[R+1]:
                        R-=1
                elif sum<0:
                    L+=1
                else:
                    R-=1
        return result