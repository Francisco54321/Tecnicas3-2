#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("REPO RVT programa triangulo ")


# In[ ]:


import math
print("Dame los tres lados que van a ser evaluados")
a=int(input("primero\n"))
b=int(input("segundo\n"))
c=int(input("tercero\n"))

#Primero tendre que identificar cual es el numero mas grande
if(a>b and a>c):
    if((a**2)==(c**2+b**2)):
        print("Los lados pueden forma5 un triangulo rectangulo")
    elif((a**2)!=(c**2+b**2)):
        print("Los lados NO pertenecen a un triangulo rectangulo")
if(b>a and b>c):
    if((b**2)==(a**2+c**2)):
        print("Los lados pueden formar un triangulo rectangulo")
    elif((b**2)!=(a**2+c**2)):
        print("Los lados NO pertenecen a un triangulo rectangulo")
if(c>b and c>a):
    if((c**2)==(a**2+b**2)):
        print("Los lados pueden forma5 un triangulo rectangulo")
    elif((c**2)!=(a**2+b**2)):
        print("Los lados NO pertenecen a un triangulo rectangulo")

