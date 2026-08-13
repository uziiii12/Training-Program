import java.util.*;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {

        int left = 0;
        long sum = 0;
        long answer = 0;

        Map<Integer, Integer> seen = new HashMap<>();

        for (int right = 0; right < nums.length; right++) {

           
            sum += nums[right];

            seen.put(nums[right],
                    seen.getOrDefault(nums[right], 0) + 1);

            
            if (right - left + 1 == k) {

               
                if (seen.size() == k) {
                    answer = Math.max(answer, sum);
                }

              
                seen.put(nums[left],
                        seen.get(nums[left]) - 1);

                if (seen.get(nums[left]) == 0) {
                    seen.remove(nums[left]);
                }

                sum -= nums[left];

                
                left++;
            }
        }

        return answer;
    }
}