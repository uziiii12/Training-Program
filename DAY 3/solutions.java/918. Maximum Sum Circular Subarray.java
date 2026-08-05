class Solution {
    public int maxSubarraySumCircular(int[] nums) {

        int total = 0;

        int curMax = nums[0];
        int maxSum = nums[0];

        int curMin = nums[0];
        int minSum = nums[0];

        for (int num : nums) {

            total += num;
        }

        for (int i = 1; i < nums.length; i++) {

            curMax = Math.max(nums[i], curMax + nums[i]);
            maxSum = Math.max(maxSum, curMax);

            curMin = Math.min(nums[i], curMin + nums[i]);
            minSum = Math.min(minSum, curMin);
        }

        if (maxSum < 0) {
            return maxSum;
        }

        return Math.max(maxSum, total - minSum);
    }
}