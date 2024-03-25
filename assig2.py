#!/usr/bin/env python
# coding: utf-8

# In[1]:


def merge_sort_with_sounds(arr):

    def merge(left, right):

        merged, i, j = [], 0, 0
        while i < len(left) and j<len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                print("Swap sound!")  # Placeholder for swap sound
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def merge_sort_recursive(arr):
        
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        return merge(left, right)

    sorted_array = merge_sort_recursive(arr)
    print("Final sorted array:", sorted_array)

# Example array to sort
array = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
merge_sort_with_sounds(array)


# In[ ]:




