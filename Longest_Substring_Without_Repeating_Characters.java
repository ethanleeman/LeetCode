class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = s.length(), max = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        int last = -1;
        for(int i = 0; i < length; i++) {
            //System.out.println("hi");
            //System.out.println(s.charAt(i));
            //System.out.println(map.get(s.charAt(i)));
            if (map.get(s.charAt(i)) != null) {
                last = Math.max(map.get(s.charAt(i)),last); }
            map.put(s.charAt(i),i);
            if (i - last > max) max = i - last;
            //System.out.println(i);
            //System.out.println(last);


        }

        return max;

    }
}
