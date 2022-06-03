'''
#Create a traversal algorithm for Breadth first traversal
graph = {
  'J' : ['A','M'],
  'A' : ['E', 'S'],
  'M' : ['B'],
  'E' : [],
  'S' : ['B'],
  'B' : []

}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'J')

'''

#Create a program that implements the concept of hashing using separate chaining.
HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print('', end=" ")
            print(j, end=" ")
        print()

# Driver Code
insert(HashTable, 11, 'Apple')
insert(HashTable, 19, 'Pineapple')
insert(HashTable, 15, 'Orange')
insert(HashTable, 29, 'Strawberry')
insert(HashTable, 25, 'Melon')
insert(HashTable, 10, 'Grapes')

display_hash(HashTable)

