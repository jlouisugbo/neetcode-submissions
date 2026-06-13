class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sum = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            sum.put(nums[i], i);
        }  
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if(sum.containsKey(difference) && sum.get(difference) != i){
                return new int[]{i,sum.get(difference)};
            }
        }
        
        return new int[]{};
    }
}