class Solution {
    public String defangIPaddr(String address) {
        String out = "";
        for(int i = 0; i < address.length(); i++) {
            if (address.charAt(i) == '.') out = out + "[.]";
            else out = out + address.charAt(i);
        }
        return out;
    }
}
