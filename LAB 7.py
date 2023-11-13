#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_node(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search_node(root.left, key)
    else:
        return search_node(root.right, key)

# Example usage
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

key = 4
result = search_node(root, key)

if result is not None:
    print("Node found!")
else:
    print("Node not found!")


# In[2]:


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leaf_node_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    return leaf_node_sum(root.left) + leaf_node_sum(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sum_of_leaf_nodes = leaf_node_sum(root)
print("Sum of leaf nodes:", sum_of_leaf_nodes)


# In[3]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printAllLevels(root):
   

    queue = [root]
    level = 1

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current = queue.pop(0)

         
            print(current.val, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
printAllLevels(root)


# In[ ]:




