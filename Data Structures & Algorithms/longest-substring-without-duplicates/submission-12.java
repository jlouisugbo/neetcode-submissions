
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length();
        
        int left = 0;
        int right = 0;
        int result = 0;
        HashSet<Character> set = new HashSet<>();

        while (right < s.length()) {
            if (!set.contains(s.charAt(right))) {
                set.add(s.charAt(right));
                right++;
                result = Math.max(result, right - left);
            } else {
                set.remove(s.charAt(left));
                left++;
            }
        }
        return result;
    }
}
