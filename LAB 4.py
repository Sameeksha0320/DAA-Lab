#!/usr/bin/env python
# coding: utf-8

# In[1]:


def diagonal_interchange(matrix):
    n = len(matrix)
    
    # Interchange the values of the left and right diagonals
    for i in range(n):
        temp = matrix[i][i]
        matrix[i][i] = matrix[i][n-i-1]
        matrix[i][n-i-1] = temp
    
    return matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

interchanged_matrix = diagonal_interchange(matrix)
print(interchanged_matrix)


# In[2]:


def find_indices(arr, num):
    indices = []
    
    for i in range(len(arr)):
        if arr[i] == num:
            indices.append(i)
    
    return indices

array = [3, 7, 2, 5, 7, 9, 7]
number = 7

indices = find_indices(array, number)
print(indices)


# In[ ]:




