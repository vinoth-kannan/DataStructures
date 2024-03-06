#Binary Tree
import collections


#defining a Tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

#Inserting a node
    def insert(self,data):
        if self.data is None:
            self.data=data
        else:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

# In - Order Traversal : leftchild - root - rightchild
def inOrderTraversal(root):
    if root is None:
        return
    else:
        inOrderTraversal(root.left)
        print(root.data,end=" ")
        inOrderTraversal(root.right)


# Pre - Order Traversal : root - leftchild - rightchild
def preOrderTraversal(root):
    if root is None:
        return
    else:
        print(root.data,end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

#Post - Order Traversal : leftchild - rightchild - root
def postOrderTraversal(root):
    if root is None:
        return
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data,end=" ")

#Adjaceny List creation  root : [ direct left child, direct right child ]
def makeList(root):
    if root is None:
        return
    else:
        d[root.data]=[]
        makeList(root.left)
        if root.left:
            d[root.data].append(root.left.data)
        if root.right:
            d[root.data].append(root.right.data)
        makeList(root.right)
    return d

# bfs - breadth first search
def bfs(aList):
    queue=collections.deque('g')
    visited=[]
    while queue:
        node=queue.popleft()
        visited.append(node)
        [queue.append(x) for x in aList[node]]
    print(visited)

print("Welcome to tree")
root=Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')

d={}
adjacencyList=makeList(root)
bfs(adjacencyList)