#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 1
h = 0
while n < 100:
    if n%3 == 0:
        print n,
        h += 1
    n += 1
print '\nEntre 1 y 100 hay %i numeros multiplos de 3' % h

