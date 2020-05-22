class Solution {
    public int removeDuplicates(int[] nums) {
        int curr = 0 , index = 0;
        if (nums.length > 0) {curr = nums[0]; index = 1;}
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] > curr){
                nums[index] = nums[i];
                index++;
                curr = nums[i];
            }
        }
        return index;
    }
}
