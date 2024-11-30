class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self,values=None):
        self.root = None
        if values:
            for value in values:
                self.insert(value)

    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, node : Node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)

    def search(self, data):
        return self.search_recursive(self.root, data)

    def search_recursive(self, node : Node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self.search_recursive(node.left, data)
        else:
            return self.search_recursive(node.right, data)

    def display(self):
        result=[]
        def inorder(node : Node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)

        inorder(self.root)
        return result

    def delete(self, data):
        self.root = self.delete_recursive(self.root, data)

    def delete_recursive(self, node : Node, data):
        if not node:
            return node 
        if data < node.data:
            node.left = self.delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self.delete_recursive(node.right, data)
        else:
            if not node.left: 
                return node.right
            elif not node.right:
                return node.left

            successor = self.min_value_node(node.right)
            node.data = successor.data
            
            node.right = self.delete_recursive(node.right, successor.data)

        return node

    def min_value_node(self, node : Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current