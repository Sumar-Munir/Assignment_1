#!/usr/bin/env python
# coding: utf-8

# In[2]:


import statistics


infected_data = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]


print("Minimum:", min(infected_data))
print("Maximum:", max(infected_data))
print("Range:", max(infected_data) - min(infected_data))
print("Mean:", statistics.mean(infected_data))
print("Median:", statistics.median(infected_data))
print("Variance:", statistics.variance(infected_data))
print("Standard Deviation:", statistics.stdev(infected_data))


# In[ ]:




