# insertion
# Python program to reverse a linked list
'''
class Node:

    # Constructor to initialize the node object
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next element


class LinkedList:

    # Function to initialize head and tail

    def __init__(self):
        self.head = None
        self.tail = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        temp = self.head  # temp variable
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Start with the empty list
    slist = LinkedList()
    slist.append(6)
    slist.push(7)
    slist.push(1)
    slist.append(4)
    slist.insertAfter(slist.head.next, 8)

    print('Created linked list is: ')
    slist.printList()
'''

'''
#doubly linked list insertion
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List
class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, newdata):

        newNode = Node(newdata)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def printList(self, node):

        while node:
            print(" {}".format(node.data))
            node = node.next


dlist = DoublyLinkedList()

dlist.push(6)
dlist.push(7)
dlist.push(1)
dlist.push(4)


dlist.printList(dlist.head)

'''

# circular

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        x = Node(newData)
        temp = self.head
        x.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = x
        else:
            x.next = x
        self.head = x

    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d" % (temp.data)),
                temp = temp.next
                if (temp == self.head):
                    break


my_list = circularLinkedList()
print("Elements are added to the list ")
my_list.push(56)
my_list.push(78)
my_list.push(12)
print("The data is : ")
my_list.printList()
