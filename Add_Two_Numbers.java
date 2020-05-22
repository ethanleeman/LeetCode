/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode((l1.val + l2.val) %10 );
        ListNode current = ans;
        ListNode run1 = l1.next;
        ListNode run2 = l2.next;
        int carry = (l1.val + l2.val) / 10;
        while (run1 != null && run2 != null) {
            ListNode add = new ListNode((run1.val + run2.val + carry) % 10 );
            carry = (run1.val + run2.val + carry)/10;
            run1 = run1.next;
            run2 = run2.next;
            current.next = add;
            current = current.next;
        }
        if (run1 == null) {
            ListNode temp = run1;
            run1 = run2;
            run2 = temp;
        }
        while (run1 != null) {
            ListNode add = new ListNode((run1.val + carry) % 10 );
            carry = (run1.val + carry)/10;
            run1 = run1.next;
            current.next = add;
            current = current.next;
        }
        if (carry != 0) {
            ListNode last = new ListNode(carry );
            current.next = last;
            current = current.next;
        }


        return ans;
    }
}
