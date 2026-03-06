"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
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


def reverse(head):
    prev = None
    current = head

    while(current is not None):
        n_elem = current.next
        current.next = prev
        prev = current
        current = n_elem

    return prev




def checkPalindrome(head):
    if head is None or head.next is None:
        return True
    

    prev = None
    slow = head
    fast = head

    while(fast.next is not None and fast.next.next is not None):
        prev = slow
        slow = slow.next
        fast = fast.next.next


    lpart, rpart = None, None

    if fast.next is None :
        # Odd Elements
        n_elem = slow.next
        prev.next = None
        lpart, rpart = head, reverse(n_elem)

    else :
        # Even Elements
        n_elem = slow.next
        slow.next = None
        lpart, rpart = head, reverse(n_elem)

    
    ptr1 = lpart
    ptr2 = rpart

    while(ptr1 is not None and ptr2 is not None):
        if ptr1.val != ptr2.val :
            return False
        
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    if (ptr1 is not None or ptr2 is not None):
        return False
    
    return True







if __name__ == "__main__":
    arr = [1,2,4,5,7,4,2,1]
    l1 = Solution(arr)
    
    print(checkPalindrome(l1.head))
