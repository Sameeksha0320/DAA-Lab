#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_triplets(arr, target_sum):
    arr.sort()  # Sort the array in ascending order
    triplets = []
    
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    
    return triplets

array = [1, 4, 2, 6, 3, 5, 7, 8, 9]
target = 15
result = find_triplets(array, target)
print(result)


# In[2]:


def counting_sort(arr):
    # Find the maximum element in the array
    max_value = max(arr)
    
    # Create a count array to store the frequency of each element
    count = [0] * (max_value + 1)
    
    # Count the frequency of each element
    for num in arr:
        count[num] += 1
    
    # Create a sorted array using the count array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

array = [0, 0, 1, 2, 0, 1, 2, 2, 1]
sorted_array = counting_sort(array)
print(sorted_array)


# In[ ]:




