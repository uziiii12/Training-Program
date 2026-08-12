import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {

        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int num : nums) {

            if (hashmap.containsKey(num)) {
                return true;
            }

            hashmap.put(num, 1);
        }

        return false;
    }
}