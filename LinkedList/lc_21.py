"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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

def mergeTwoLists(l1_head, l2_head):
    if l1_head is None :
        return l2_head

    if l2_head is None:
        return l1_head
    
    current_l1 = l1_head
    current_l2 = l2_head

    head = None
    prev_elem = None

    while(current_l1 is not None and current_l2 is not None):
        if current_l1.val <= current_l2.val :
            if head is None :
                head = current_l1
                prev_elem = current_l1
                current_l1 = current_l1.next

            else :
                prev_elem.next = current_l1
                prev_elem = current_l1
                current_l1 = current_l1.next
                
        else :
            if head is None :
                head = current_l2
                prev_elem = current_l2
                current_l2 = current_l2.next

            else :
                prev_elem.next = current_l2
                prev_elem = current_l2
                current_l2 = current_l2.next

    while current_l1 is not None :
        prev_elem.next = current_l1
        prev_elem = current_l1
        current_l1 = current_l1.next


    while current_l2 is not None:
        prev_elem.next = current_l2
        prev_elem = current_l2
        current_l2 = current_l2.next


    return head
    


if __name__ == "__main__" :
    arr1 = []
    arr2 = [0]
    l1 = Solution(arr1)
    l1.traverse()
    print("")
    print("=============")
    l2 = Solution(arr2)
    l2.traverse()
    print("")
    print("=============")
    print()
    
    new_head = mergeTwoLists(l1.head, l2.head)
    current = new_head

    while current is not None :
        print(current.val)
        current = current.next
