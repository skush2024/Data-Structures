"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def __init__(self, arr:list):
        prev_node = None
        for i in range(len(arr)):
            if i == 0 :
                self.head = ListNode(arr[i])
                prev_node = self.head
                continue

            new_node = ListNode(arr[i])
            prev_node.next = new_node
            prev_node = new_node

    def traverse(self) :
        current = self.head

        while current is not None: 
            print(current.val)
            current = current.next

def addTwoNumbers(l1, l2):
    current_l1 = l1
    current_l2 = l2

    head = None
    prev_elem = None
    carry = 0

    while(current_l1 is not None and current_l2 is not None):
        node_val = (current_l1.val + current_l2.val + carry) % 10
        carry = (current_l1.val + current_l2.val + carry) // 10
        node = ListNode(node_val)
        if head is None :
            head = node
            prev_elem = node
        
        else :
            prev_elem.next = node
            prev_elem = node

        current_l1 = current_l1.next
        current_l2 = current_l2.next

    while(current_l1 is not None):
        node_val = (current_l1.val + carry) % 10
        carry = (current_l1.val + carry) // 10
        node = ListNode(node_val)

        if head is None :
            head = node
            prev_elem = node
        
        else :
            prev_elem.next = node
            prev_elem = node

        current_l1 = current_l1.next

    while(current_l2 is not None):
        node_val = (current_l2.val + carry) % 10
        carry = (current_l2.val + carry) // 10
        node = ListNode(node_val)

        if head is None :
            head = node
            prev_elem = node
        
        else :
            prev_elem.next = node
            prev_elem = node

        current_l2 = current_l2.next

    
    if carry == 1 :
        node = ListNode(1)
        prev_elem.next = node

    return head
        
        
    




if __name__ == "__main__" :
    arr = [2,4,9]
    arr2 = [5,6,4,9]
    l1 = Solution(arr)
    l2 = Solution(arr2)
        
    head = addTwoNumbers(l1.head, l2.head)

    current = head
    
    while(current is not None):
        print(current.val)
        current = current.next
