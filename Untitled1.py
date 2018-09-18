
# coding: utf-8

# In[68]:

import numpy as np
import matplotlib.pyplot as plt
import scikit as sc
"""The input vector is a 2 dimensional vector of size a*b where a is the number of samples and x is the features."""

"""Standardize data so that each feature has mean 0 and std 1. If the std along a column is 0 this function
returns an error.
X : Input data in the form of a vector
"""
def rescaleData(X):
    s = std(X, axis = 0)
    return (X-np.mean(X, axis = 0))/std(X, axis = 0)


"""Rescale the data so that all values are between 0 and 1.
X : Input data in the form of a vector"""
def fuzzyEncoding(X):
    l = np.min(X, axis = 0)
    return (X-l)/(np.max(X, axis = 0) - l)

"""Perform the fuzzy and operation that works by taking the minimum out of two values. 
E.g. FuzzyAnd(1,3) = 1 since 1<3.
X,y : input in the form of a list
"""
def fuzzyAnd(X, Y):
    return np.minimum(X, Y)
    
"""At each row X(j,:) of an input vector X (corresponding to a sample witha  set of feature) add
the complement of the features such that X(j,:) = [X(j,:) (1-X(j,:))]."""
def addComplement(X):
    return np.hstack((X, 1-X))


# In[67]:




# In[ ]:



