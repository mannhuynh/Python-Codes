"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""
class Element(object):
    """ class Element will hold value and pointer next to the next element """

    def __init__(self, value):
        self.value = value                  # declare value property
        self.next = None                    # property next is initialize None

class LinkedList(object):
    """ Initialine the header with None value in it """
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else: 
            self.head = new_element
            
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
            
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value ==  value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    
# Test cases
# Set up some Elements - instanciate e1 to e5 with values 1 to 5
e1 = Element(1)         
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Start setting up a LinkedList 
# Instanciate ll with LinkedList and pass object e1 into it and then append 
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)


print(ll.head.value)                        # 1 - print the header, which value is 1
print(ll.head.next.value)                   # 2 - next node has value of 2    
print(ll.head.next.next.value)              # 3 - and so on
print(ll.head.next.next.next.value)         # 4 - value of e4
print(ll.head.next.next.next.next.value)    # 5 - e5 value is appended

# Test position
# The Linked List now is 1, 2, 3, 4, 5
print(ll.get_position(3).value)             # 3 - the value of the node number 3

# Test insert
ll.insert(e5,3)                             # Insert the value of e5 (5) into position 3
# the Linked List now is 1, 2, 5, 3, 4, 5
print(ll.get_position(3).value)             # 4 - the value at position 3 is 4 now

# Test delete
ll.delete(1)                                # Delete the position 1 (header)
print(ll.get_position(1).value)             # 2 - value of header (1) has been deleted
# the Linked List now is 2, 5, 3, 4, 5
print(ll.get_position(2).value)             # 5 - position 3 (value of 5) become position 2
print(ll.get_position(3).value)             # 3 - 
