class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        int left = 0;
        int windowSum = 0;
        int ans = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {

            windowSum += nums[right];

            while (windowSum >= target) {

                ans = Math.min(ans, right - left + 1);

                windowSum -= nums[left];
                left++;
            }
        }

        if (ans == Integer.MAX_VALUE) {
            return 0;
        }

        return ans;
    }
}