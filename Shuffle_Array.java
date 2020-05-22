class Solution {
    int[] org;
    int[] shuf;


    public Solution(int[] nums) {
        org = nums;
        shuf = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            shuf[i] = org[i];
        }
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return org;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        for(int i = org.length-1; i > 0; i--) {
            int k = (int) (Math.random()*(i+1));
            int temp = shuf[i];
            shuf[i] = shuf[k];
            shuf[k] = temp;
        }
        return shuf;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
