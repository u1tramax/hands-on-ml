from linkedlist import LinkedList

class Queue(LinkedList):

    def __init__(self):
        super().__init__()
        self.tail = None

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.head.data
    
    def append(self, data):
        raise AttributeError("Use enqueue() instead")

    def insert(self, index, data):
        raise AttributeError("Cannot insert at arbitrary position in Queue")

    def remove(self, index):
        raise AttributeError("Cannot remove at arbitrary position in Queue")
    
    def __repr__(self):
        return f'Queue([{list(self)}])'
