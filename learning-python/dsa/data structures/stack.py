from linkedlist import LinkedList

class Stack(LinkedList):
    
    def __init__(self):
        super().__init__()

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    
    def append(self, data):
        raise AttributeError("Use push() instead")

    def insert(self, index, data):
        raise AttributeError("Cannot insert at arbitrary position in Stack")

    def remove(self, index):
        raise AttributeError("Cannot remove at arbitrary position in Stack")
    
    def __repr__(self):
        return f'Stack([{list(self)}])'
