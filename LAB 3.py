#!/usr/bin/env python
# coding: utf-8

# In[1]:


def remove_duplicates(arr):
    if not arr:
        return []

    unique_elements = []
    for item in arr:
        if item not in unique_elements:
            unique_elements.append(item)

    return unique_elements


input_list = [1, 12, 11, 10, 11, 1]
result = remove_duplicates(input_list)
print(result)  


# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_loop(head):
    if head is None or head.next is None:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    return True


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  

has_loop_result = has_loop(head)
print(has_loop_result)


# In[ ]:




