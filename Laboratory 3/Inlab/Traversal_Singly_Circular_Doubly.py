'''
# Creating node class of the singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Creating addNode() to add newly created nodes.
    def append(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # Creating display() to print newly created nodes via traversing.
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


s = SinglyLinkedList()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data = int(input('Enter data: '))
    s.append(data)
print('The linked list: ', end='')
s.printList()
'''

'''
# Class to create a Doubly Linked List
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # Check if the list is empty
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            return
        n = self.head
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        newNode = Node(data)
        n.next = newNode
        newNode.prev = n


    # Traversing and Displaying each element of the list
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")



dList = doublyLinkedList()

dList.append(20)
dList.append(30)
dList.append(40)
dList.append(50)
dList.append(60)
dList.Display()

'''
#circular

# Python program to demonstrate
# circular linked list traversal

# Structure for a Node
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break


# Driver program to test above function

# Initialize list as empty
cllist = CircularLinkedList()

# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)

print("Contents of circular Linked List")
cllist.printList()
