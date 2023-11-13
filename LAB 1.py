#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_leaders(arr):
    leaders = []
    max_val = float('-inf')
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= max_val:
            leaders.append(arr[i])
            max_val = arr[i]
    
    leaders.reverse()
    return leaders

# Example usage
array = [16, 17, 4, 3, 5, 2]
result = find_leaders(array)
print(result)


# In[2]:


def alternate_sort(arr):
    arr.sort()  # Sort the array in ascending order
    output = []
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if left == right:
            output.append(arr[left])
        else:
            output.append(arr[left])
            output.append(arr[right])
        
        left += 1
        right -= 1
    
    return output

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = alternate_sort(array)
print(result)


# In[ ]:




