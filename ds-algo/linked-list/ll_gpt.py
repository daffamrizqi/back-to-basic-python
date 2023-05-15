class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def delete_node(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous_node.next = current_node.next
                    if current_node.next is None:
                        self.tail = previous_node
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False
    
    def insert_node(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current_node = self.head
            current_index = 0
            while current_node is not None and current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            if current_node is None:
                return False
            else:
                new_node.next = current_node.next
                current_node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
        return True
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
