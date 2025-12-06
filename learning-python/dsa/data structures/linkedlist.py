class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0:
            raise ValueError('Index is negative')
        if index == 0:
            new_head = self.Node(data)
            new_head.next = self.head
            self.head = new_head
            self.size += 1
            return
        current = self.head
        n = 0
        while n < index - 1 and current:
            current = current.next
            n += 1
        if current is None:
            raise IndexError('Index out of bounds')
        new_node = self.Node(data)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def remove(self, index):
        if index < 0:
            raise ValueError('Index is negative')
        if index == 0:
            if self.head:
                self.head = self.head.next
                self.size -= 1
            return
        current = self.head
        n = 0
        while n < index - 1 and current:
            current = current.next
            n += 1
        if current.next is None:
            raise IndexError('Index out of bounds')
        current.next = current.next.next
        self.size -= 1

    def get(self, index):
        if self.head == None:
            raise ValueError('List is empty')
        current = self.head
        n = 0
        while n < index and current:
            current = current.next
            n += 1
        if current is None:
            raise IndexError("Index out of bounds")
        return current.data
        
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f'LinkedList({list(self)})'
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        return self.get(index)

    def is_empty(self):
        return self.head is None
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
