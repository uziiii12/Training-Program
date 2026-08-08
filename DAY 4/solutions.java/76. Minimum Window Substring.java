import java.util.*;

class Solution {
    public String minWindow(String s, String t) {

        if (t.length() > s.length()) {
            return "";
        }

        HashMap<Character, Integer> need = new HashMap<>();

        for (char ch : t.toCharArray()) {
            need.put(ch, need.getOrDefault(ch, 0) + 1);
        }

        HashMap<Character, Integer> window = new HashMap<>();

        int left = 0;
        int have = 0;
        int needCount = need.size();

        int minLength = Integer.MAX_VALUE;
        String answer = "";

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            window.put(ch, window.getOrDefault(ch, 0) + 1);

            if (need.containsKey(ch) &&
                window.get(ch).intValue() == need.get(ch).intValue()) {

                have++;
            }

            while (have == needCount) {

                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    answer = s.substring(left, right + 1);
                }

                char leftChar = s.charAt(left);

                window.put(
                    leftChar,
                    window.get(leftChar) - 1
                );

                if (need.containsKey(leftChar) &&
                    window.get(leftChar) < need.get(leftChar)) {

                    have--;
                }

                left++;
            }
        }

        return answer;
    }
}