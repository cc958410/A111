# -*- coding: utf-8 -*-
"""解一元二次方程式(H)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_YoisIkwcLH8po8914cAWD95VR--TjSj
"""

def compute(a,b,c):
 q=(b**2-4*a*c)**(0.5)
 return(-b+q)/(2*a),(-b-q)/(2*a)

a=eval(input())
b=eval(input())
c=eval(input())
print(compute (a,b,c))