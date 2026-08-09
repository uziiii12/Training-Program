class Solution {
    public int shipWithinDays(int[] weights, int days) {

        int left = 0;
        int right = 0;

        for (int weight : weights) {
            left = Math.max(left, weight);
            right += weight;
        }

        while (left < right) {

            int capacity = left + (right - left) / 2;

            int currentWeight = 0;
            int requiredDays = 1;

            for (int weight : weights) {

                if (currentWeight + weight > capacity) {
                    requiredDays++;
                    currentWeight = 0;
                }

                currentWeight += weight;
            }

            if (requiredDays <= days) {
                right = capacity;
            } else {
                left = capacity + 1;
            }
        }

        return left;
    }
}