
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length();
        
        int left = 0;
        int right = 0;
        int result = 0;
        HashSet<Character> set = new HashSet<>();

        while (right < s.length()) {
            if (!set.contains(s.charAt(right))) {
                // If the character is not in the set, add it
                set.add(s.charAt(right));
                right++;
                // Update result with the maximum window size
                result = Math.max(result, right - left);
            } else {
                // If the character is a duplicate, remove the character at 'left' and move 'left' forward
                set.remove(s.charAt(left));
                left++;
            }
        }
        return result;
    }
}
