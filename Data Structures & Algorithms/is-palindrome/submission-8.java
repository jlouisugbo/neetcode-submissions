class Solution {
    public boolean isPalindrome(String s) {
        ArrayList<Character> aStr = new ArrayList<Character>();
        for (int i = 0; i < s.length(); i++){
            char chara = Character.toLowerCase(s.charAt(i));
            if(Character.isLetterOrDigit(chara)){
                aStr.add(chara);
            }
        }
        int left = 0;
        int right = aStr.size() - 1;
        
        while (left < right) {
            if (!aStr.get(left).equals(aStr.get(right))) {
                return false;  // Not a palindrome if any mismatch is found
            }
            left++;
            right--;
        }
        
        return true;
    }
}
