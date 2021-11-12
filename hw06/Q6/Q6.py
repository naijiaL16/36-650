# Q6

class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Reverse Linked List
class ReversedLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

# Find length of Linked List
    def size(self):
        if self.tail == None:
            return 0

        size = 0
        current = self.tail
        while current:
            size += 1
            current = current.previous

        return size        
            
    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.tail
        node.previous = current
        self.tail = node          
            
    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if tail node is to be deleted
        if self.tail.data == data:
            tail = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return

    # search a node in a linked list
    def search(self, data):
        if not self.tail:
            raise ValueError("List is empty")

        temp = self.tail

        # Check if tail node is tail of the list
        if self.tail.data == data:
            print("true")
            return

        while temp.previous:
            if temp.previous.data == data:
                print("true")
                return
            temp = temp.previous

        print("Node not found")
        return

# insert function
first_node = Node(17)
linked_list = ReversedLinkedList(first_node)
linked_list.insert(12)
linked_list.insert(9)
linked_list.insert(87)
linked_list.insert(46)
linked_list.insert(37)

print("The Reversed Linked List is:")
linked_list.print_list()

print(linked_list.size())


# delete function
linked_list.delete(46)
print("After deleting 46, the Linked List is:")
linked_list.print_list()
print("Current Size of the Linked List is:")
print(linked_list.size())


# search function
linked_list.search(37)
linked_list.search(87)
linked_list.search(7)