class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

   
def getLL(arr: list):
    head = None
    prev_node = None

    for i in range(len(arr)):
        node = Node(arr[i])
        if i == 0 :
            head = node
        else :
            prev_node.next = node
    
        prev_node = node 
    
    return head


def insertElem(head:Node, pos:int, elem:int):
    if pos == 0 :
        node = Node(elem)
        node.next = head
        return node

    count = 0
    start = head
    while (count < pos - 1):
        count += 1
        start = start.next
    
    inserted = Node(elem)
    n_elem = start.next
    start.next = inserted
    inserted.next = n_elem
    return head
    

def deleteElem(head:Node, pos:int):
    if pos == 0 :
        return head.next
    
    current = head
    count = 0
    while(count < pos - 1):
        count += 1
        current = current.next
    
    n_elem =current.next.next
    current.next = n_elem
    return head





if __name__ == "__main__" :
    head = getLL([2,3,4,5])
    head = insertElem(head, 4,10)
    head = deleteElem(head, 2)

    node = head

    while(node is not None) :
        print(node.data)
        node = node.next


    