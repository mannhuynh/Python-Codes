"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue():
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
print(q.peek())                 # 1 -  first element with value 1

# Test dequeue
print(q.dequeue())              # 1 - took the first element out

# Test enqueue
q.enqueue(4)
print(q.dequeue())              # 2 - the second element becomes the first element 
print(q.dequeue())              # 3 - the third element becomes the first element 
print(q.dequeue())              # 4 - the fourth element becomes the first element 

q.enqueue(5)
print(q.peek())                 # 5 - the fifth element is the head of the queue
