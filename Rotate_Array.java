class Solution {
    public int gcd(int a, int b){
        if (b == 0) return 0;
        if (b < 0) b = -b;
        while (b > 0) {
            a = a % b;
            int temp = a;
            a = b;
            b = temp;
        }
        return a;
    }

    public void rotate(int[] nums, int k) {
        int g = gcd(nums.length,k);
        int adder = nums.length;
        if (adder < k) {
            adder += nums.length;
        }
       for(int curr = 0; curr < g; curr++){
           int mem = nums[curr];
           do {
               nums[curr] = nums[(curr-k+adder) %nums.length];
               curr = (curr-k+adder) %nums.length;
           }
           while (curr >= g );
           nums[(curr+k+adder) %nums.length] = mem;
       }
    }
}
