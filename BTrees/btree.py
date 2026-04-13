class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        pass

    def buildTree(seld, tree_dict, root_node):
        nodes = {}

        for val in tree_dict:
            nodes[val] = Node(val)

        for val, (left, right) in tree_dict.items():
            if left is not None :
                nodes[val].left = nodes[left]
            
            if right is not None:
                nodes[val].right = nodes[right]
        
        return nodes[root_node]

    def dfsPreOrder(self,node):

        if not node:
            return 
        
        print(node.val, end=" -> ")         
        self.dfsPreOrder(node.left)
        self.dfsPreOrder(node.right)

    def dfsInOrder(self, node):
        if node is None :
            return

        self.dfsInOrder(node.left)
        print(node.val, end = " -> ")
        self.dfsInOrder(node.right) 

    def dfsPostOrder(self, node):
        if node is None :
            return
        
        self.dfsPostOrder(node.left)
        self.dfsPostOrder(node.right)
        print(node.val, end =" -> ")

    def bfs(self, node):
        if node is None :
            return
        
        queue = [node]
        front = 0

        while front < len(queue):
            n = queue[front]
            print(n.val, end = " -> ")
            
            if n.left:
                queue.append(n.left)
            
            if n.right :
                queue.append(n.right)
            
            front += 1


if __name__ == "__main__":
    tree = {
        1: [2,3],
        2: [4,5],
        3: [6,7],
        4: [None, None],
        5: [8, None],
        6: [None, None],
        7: [9, 10],
        8: [None, None],
        9: [None, None],
        10: [None, None]
    }

    solver = Solution()
    root = solver.buildTree(tree, 1)
    print(f" Inorder: {solver.dfsInOrder(root)}")
    print(f" Preorder: {solver.dfsPreOrder(root)}")
    print(f" Postorder: {solver.dfsPostOrder(root)}") 

    print(f" BFS: {solver.bfs(root)}")