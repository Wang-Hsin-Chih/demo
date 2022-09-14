#!/usr/bin/env python
# coding: utf-8

# In[6]:


import argparse

parser=argparse.ArgumentParser()

parser.add_argument("package")

parser.add_argument("totalEvent")

#... 还可以添加更多其它参数

args=parser.parse_args()

param=vars(args)

v={}

for key,value in param.items():
    v[key]=value
    print(v)


# In[ ]:




