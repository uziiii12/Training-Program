import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        HashSet<Integer> set1 = new HashSet<>();

        for (int num : nums1) {
            set1.add(num);
        }

        HashSet<Integer> answer = new HashSet<>();

        for (int num : nums2) {
            if (set1.contains(num)) {
                answer.add(num);
            }
        }

        int[] result = new int[answer.size()];

        int i = 0;

        for (int num : answer) {
            result[i] = num;
            i++;
        }

        return result;
    }
}