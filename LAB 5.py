#!/usr/bin/env python
# coding: utf-8

# In[3]:


matrix = [
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]

max_row = -1
max_count = -1

for i, row in enumerate(matrix):
    count_ones = row.count(1)
    
  
    if count_ones > max_count:
        max_row = i
        max_count = count_ones

print(f"Row {max_row + 1} has the most ones with {max_count} ones.")


# In[4]:


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

num_rows = len(matrix)
num_cols = len(matrix[0])

middle_row = matrix[num_rows // 2]
middle_col = [matrix[i][num_cols // 2] for i in range(num_rows)]

intersecting_element = matrix[num_rows // 2][num_cols // 2]

total_sum = sum(middle_row) + sum(middle_col) - intersecting_element

print("Sum of middle row and middle column with intersecting element added once:", total_sum)


# In[ ]:




