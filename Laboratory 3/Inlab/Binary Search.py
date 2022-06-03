# binary search
# A. Create a binary search tree.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def displayTree(self):
        print(self.data)


root = Node(10)
root.displayTree()


# B. Traverse the above binary search tree recursively in pre-order, post-order and in-order.

# pre-order
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    print(str(root.data) + "->", end='')
    preorder(root.left)
    preorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    print("\nPreorder Traversal")
    preorder(root)


# inorder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    preorder(root.left)
    print(str(root.data) + "->", end='')
    preorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    print("\nInorder Traversal")
    inorder(root)


# postorder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return

    preorder(root.left)
    preorder(root.right)
    print(str(root.data) + "->", end='')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    print("\nPostorder Traversal")
    postorder(root)

# C. Count the number of nodes in the binary search tree.
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def leftHeight(Node):
    ht = 0
    while (Node):
        ht += 1
        Node = Node.left

    return ht

def rightHeight(Node):
    ht = 0
    while (Node):
        ht += 1
        Node = Node.right

    return ht


def TotalNodes(root):
    # Base case
    if (root == None):
        return 0

    lh = leftHeight(root)
    rh = rightHeight(root)

    if (lh == rh):
        return (1 << lh) - 1

    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(9)
root.right.right = Node(8)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
print("\nNumber of Nodes:")
print(TotalNodes(root))


