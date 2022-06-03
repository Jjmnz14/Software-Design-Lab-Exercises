# A simple Python program for traversal of a linked list
'''
#Singly linked list
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    slist = LinkedList()
    slist.head = Node(1)
    second = Node(2)
    third = Node(3)
    slist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node

    slist.printList()

'''


'''
    #doubly
    # Represent a node of doubly linked list
class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # Append an item
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.data),
            current = current.next


items = doubly_linked_list()

items.append('Spain')
items.append('France')
items.append('Philippines')
items.append('US')
items.append('Japan')
items.append('Korea')

items.display()

'''

# circularly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # This function will add the new node at the end of the list.
    def add(self, data):
        newNode = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    # Displays all the nodes in the list
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the circular linked list: ")
            print(current.data),
            while current.next != self.head:
                current = current.next
                print(current.data),


cl = CreateList()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(4)
cl.display()
