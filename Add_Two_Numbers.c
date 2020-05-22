/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ans;
    ans = (struct ListNode*) malloc(sizeof(struct ListNode));
    ans->next = NULL;
    ans->val = (l1->val + l2->val) %10;

    struct ListNode* current = ans;
    struct ListNode* run1 = l1->next;
    struct ListNode* run2 = l2->next;
    int carry = (l1->val + l2->val) / 10;
    while (run1 != NULL && run2 != NULL) {
        struct ListNode* add = (struct ListNode*) malloc(sizeof(struct ListNode));
        add->next = NULL;
        add->val = (run1->val + run2->val + carry) % 10;
        carry = (run1->val + run2->val + carry)/10;
        run1 = run1->next;
        run2 = run2->next;
        current->next = add;
        current = current->next;
        }
        if (run1 == NULL) {
            struct ListNode* temp = run1;
            run1 = run2;
            run2 = temp;
        }
        while (run1 != NULL) {
            struct ListNode* add = (struct ListNode*) malloc(sizeof(struct ListNode));
            add->next = NULL;
            add->val = (run1->val + carry) % 10;
            carry = (run1->val + carry)/10;
            run1 = run1->next;
            current->next = add;
            current = current->next;
        }
        if (carry != 0) {
            struct ListNode* last = (struct ListNode*) malloc(sizeof(struct ListNode));
            last->next = NULL;
            last->val = (carry) % 10;
            current->next = last;
            current = current->next;
        }





    return ans;
}
