class BinaryTree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._append_recursive(self.root, data)

    def _append_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = self.Node(data)
            else:
                self._append_recursive(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = self.Node(data)
            else:
                self._append_recursive(current_node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if current_node is None:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def remove(self, data):
        pass

    def traversal(self, type='inorder'):
        result = []
        self._traversal_recursive(self.root, result, type)
        return result
    
    def _traversal_recursive(self, current_node, result, type):
        if current_node is None:
            return
        
        if type == 'preorder':
            result.append(current_node.data)

        self._traversal_recursive(current_node.left, result, type)

        if current_node == 'inorder':
            result.append(current_node.data)

        self._traversal_recursive(current_node.right, result, type)

        if type == 'postorder':
            result.append(current_node.data)