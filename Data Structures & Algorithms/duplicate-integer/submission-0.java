class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dupe = new HashSet<Integer>();
        for(int num : nums){
            dupe.add(num);
        }
        return nums.length != dupe.size();
    }
}
