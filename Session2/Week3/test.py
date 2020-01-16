# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:26:27 2020

@author: sonyu
"""

M = [[(0, 0) for i in range(6)] for j in range(5)]
for item in M:
    print (item)
print("--------------------SECOND-----------------")
fromM = 1
M[1][1] = M[0][0][0] + 7, fromM
for item in M:
    print (item)