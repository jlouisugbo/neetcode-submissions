class Solution {
    public int maxProfit(int[] prices) {
        int i = 0;
        int j = 1;
        if(prices.length <= 2){
            if(prices.length==1) return 0;
            if(prices[j]>prices[i]){
                return prices[j] - prices[i];
            }
            return 0;
        } 
        int result = Math.max(prices[j]-prices[i],0);
        while(i < prices.length-1 && j < prices.length-1){
            if (prices[j] > prices[i] || prices[i] == prices[j]) {
                j++;
            } else if (prices[i] > prices[j]) {
                i++;
                j = i+1;
            }
            result = Math.max(prices[j]-prices[i],result);
        }
        return result;
    }
}
