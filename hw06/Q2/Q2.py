# Q2

class Queue:
    # member variable
    inner_list = []

    # member function
    def enqueue(self, value):
        self.inner_list.insert(0, value)
        
    def dequeue(self):
        return self.inner_list.pop()
        
    def delete(self, value):
        lst_len = len(self.inner_list)
        for _ in range(lst_len):
            tail = self.dequeue()
            if tail != value:
                self.enqueue(tail)


object = Queue()
object.enqueue(5)
object.enqueue(7)
object.enqueue(8)
object.enqueue(10)

object.delete(5)
print(object.inner_list)

