from disp import *
import matplotlib.pyplot as plt
import numpy as np


# ================== CLASSIFYING IMAGES ================== #
# One hot encoding
categories = np.array(['t-shirt', 'dress', 'shoe'])
n_categories = len(categories)
# We Initialize an array of zeros
ohe_labels = np.zeros((len(labels), n_categories)) # OHE stands for One Hot Encoding

# Iterate over a list of lables
for ii in range(len(labels)):
    # Find the location of the label in categories
    jj = np.where(categories == labels[ii])
    # Set the corresponding zero to one
    ohe_labels[ii, jj] = 1

# One-Hot Encoding Testing Predictions
    
