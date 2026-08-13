import java.util.*;

class Solution {
    public int maxVowels(String s, int k) {

        int left = 0;
        int count = 0;
        int answer = 0;

        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        for (int right = 0; right < s.length(); right++) {

            if (vowels.contains(s.charAt(right))) {
                count++;
            }

            if (right - left + 1 == k) {

                answer = Math.max(answer, count);

                if (vowels.contains(s.charAt(left))) {
                    count--;
                }

                left++;
            }
        }

        return answer;
    }
}