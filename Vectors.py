"""
Vectors.py
A series of functions used to manipulate vectors in python
where vectors are represented by lists.
Author: Matthew Klein
"""

import math


# Returns the magnitude of a 3-dimensional vector
def magnitude(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)


# Returns the normalized version of a vector
def normalize(vector):
    new_vector = []
    for i in range(len(vector)):
        new_vector.append(vector[i]/magnitude(vector))
    return new_vector


# Returns the dot product of 2 vectors
def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


# Adds 2 vectors
def addition(v1, v2):
    added = []
    for i in range(3):
        added.append(v1[i] + v2[i])
    return added


#  Subtracts 2 vectors
def subtraction(v1, v2):
    sub = []
    for i in range(3):
        sub.append(v1[i] - v2[i])
    return sub


#  Scales a vector by a given number
def scalar(num, vector):
    scale = []
    for i in range(3):
        scale.append(num*vector[i])
    return scale