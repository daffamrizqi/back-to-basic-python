class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, data):
        # delete the first node with a given data
        current = self.head
        if current.data == data:
            self.head = current.next
        else:
            while current:
                if current.data == data:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """
        Insert a new node at the given position. Assume
        the first position is "1". So inserting at position 3 means 
        between the 2nd and 3rd elements
        """
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count +1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
        pass

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


node1 = Node(1) 
node2 = Node(2)
node3 = Node(3)


ll = LinkedList(node1)
ll.append(node1)
ll.append(node2)
ll.insert(node3, 2)
ll.print()
