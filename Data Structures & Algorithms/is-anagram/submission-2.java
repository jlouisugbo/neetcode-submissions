class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        ArrayList<Character> ana1 = new ArrayList<Character>();
        ArrayList<Character> ana2 = new ArrayList<Character>();
        for (int i = 0; i < s.length(); i++){
            ana1.add(s.charAt(i));
            ana2.add(t.charAt(i));
        }
        Collections.sort(ana1);
        Collections.sort(ana2);
        return ana1.equals(ana2);
    }
}
