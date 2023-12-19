# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:21:09 2023

@author: Arslan
"""

# Linear Search
def linear_search(data, key):
    for i, item in enumerate(data):
        if item == key:
            return i
    return -1

# Test the linear search
data = ['A', 'B', 'C', 'D', 'E']
search_key = 'C'
result = linear_search(data, search_key)
print(f"Linear Search: {search_key} found at index {result}" if result != -1 else f"{search_key} not found")
