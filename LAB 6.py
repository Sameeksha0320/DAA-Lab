#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sort_matrix(matrix):
    flattened = []
    for row in matrix:
        flattened.extend(row)
    
    n = len(flattened)
    for i in range(n-1):
        for j in range(n-i-1):
            if flattened[j] > flattened[j+1]:
                flattened[j], flattened[j+1] = flattened[j+1], flattened[j]
    
    sorted_matrix = []
    for i in range(0, n, len(matrix[0])):
        sorted_matrix.append(flattened[i:i+len(matrix[0])])
    
    for i in range(len(sorted_matrix)):
        sorted_matrix[i][i] = 0
        sorted_matrix[i][len(sorted_matrix)-i-1] = 0
    
    return sorted_matrix

matrix = [[3, 2, 5],
          [1, 4, 6],
          [7, 9, 8]]

sorted_and_replaced_matrix = sort_matrix(matrix)
print(sorted_and_replaced_matrix)


# In[2]:


multiply = lambda x, y: 0 if y == 0 else x + multiply(x, y - 1)

print(multiply(3,3))

