'''
#singly linked list deletion
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

    def append(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    def printList(self):
        temp = self.head  # temp variable
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Start with the empty list
    slist = LinkedList()
    slist.append(6)
    slist.append(7)
    slist.append(1)
    slist.append(4)

    print("Created Linked List: ")
    slist.printList()
    slist.deleteNode(1)
    print("\nLinked List after Deletion of 1:")
    slist.printList()
'''
'''
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

    def pop(self, position):
        if position < 1:
            print("\nposition should be >= 1.")
        elif position == 1 and self.head != None:
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if self.head != None:
                self.head.prev = None
        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp != None:
                    temp = temp.next
            if temp != None and temp.next != None:
                nodeToDelete = temp.next
                temp.next = temp.next.next
                if temp.next.next != None:
                    temp.next.next.prev = temp.next
                nodeToDelete = None
            else:
                print("\nThe node is already null.")

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
print("after pop")
dlist.pop(2)
dlist.printList(dlist.head)

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, my_data):
        ptr_1 = Node(my_data)
        temp = self.head
        ptr_1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1

    def pop(self):
        if (self.head != None):
            if (self.head.next == self.head):
                self.head = None
            else:
                temp = self.head
                firstNode = self.head
                while (temp.next != self.head):
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                firstNode = None

    def PrintList(self):
        temp = self.head
        if (temp != None):
            print("The list contains:", end=" ")
            while (True):
                print(temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
            print()
        else:
            print("The list is empty.")


my_list = circularLinkedList()
print("Elements are added to the list ")
my_list.push(56)
my_list.push(78)
my_list.push(12)
my_list.PrintList()
print("after pop : ")
my_list.pop()
my_list.PrintList()
