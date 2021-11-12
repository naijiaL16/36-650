# Q5

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

# Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size        

# Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node            
            
    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return

    def removeduplicates(self):
        if self.head == None:
            raise ValueError("List is empty")
        # iterate through the linked list
        current = self.head
        new_list = set()
        size = self.size
        while current:
            new_list.add(current.data)
            current = current.next
        return new_list

first_node = Node(38)
linked_list = LinkedList(first_node)
linked_list.insert(2)
linked_list.insert(42)
linked_list.insert(9)
linked_list.insert(7)
linked_list.insert(9)
linked_list.insert(9)
linked_list.insert(123)
linked_list.insert(9)
linked_list.insert(57)

print("The duplicated Linked List is:")
linked_list.print_list()

print("The unduplicated Linked List is:")
linked_list.removeduplicates()