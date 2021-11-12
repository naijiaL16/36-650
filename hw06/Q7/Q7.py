
class Node:
    def __init__(self, data):
      self.toobig = None
      self.big = None
      self.small = None
      self.data = data


    def insert(self, data):

        # too big tree
        if data - self.data >= 10:
            if self.toobig:
                self.toobig.insert(data)
            else:
                self.toobig = Node(data)
        
        # big tree
        elif (data - self.data < 10) and (data - self.data >= 0) :
            if self.big:
                self.big.insert(data)
            else:
                self.big = Node(data)
        
        # small tree
        else:
            if self.small:
                self.small.insert(data)
            else:
                self.small = Node(data)
    

    def in_order_traversal(self):
        if self.small:
            self.small.in_order_traversal()
        print(self.data)
        if self.big:
            self.big.in_order_traversal()
        if self.toobig:
            self.toobig.in_order_traversal()
    

    def delete(self, data):
        all_val = []
        self.traversal_return(all_val)
        # enter the new tree
        self.toobig = None
        self.big = None
        self.small = None
        self.data = None

        # iterate through the tree
        for value in all_val:
            if value == data:
                continue
            if not self.data:
                self.data = value
            else:
                self.insert(value)
    
    def traversal_return(self, return_values = one):
        if self.small:
            self.small.traversal_return(return_values)
        if return_values is not None:
            return_values.append(self.data)
        if self.big:
            self.big.traversal_return(return_values)
        if self.toobig:
            self.toobig.traversal_return(return_values)

root = Node(20)
root.insert(40)
root.insert(29)
root.insert(45)
root.insert(32)
root.insert(12)

print("In order Traversal before deleting:")
root.in_order_traversal()

root.delete(45)
print("In order Traversal after deleting:")
root.in_order_traversal()