#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 16:00:02 2025

@author: praneshdara
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.integrate as spi
import os

training_solutions = pd.read_csv("training_solutions_rev1.csv")

training_pictures = [os.path.join('images_training_rev1', f) for f in sorted(os.listdir('images_training_rev1'))]
test_pictures = [os.path.join('images_test_rev1', f) for f in sorted(os.listdir('images_test_rev1'))]

all_ones = pd.read_csv('all_ones_benchmark.csv')
all_zeroes = pd.read_csv('all_zeros_benchmark.csv')

def read_image(file_path):
    image = cv2.imread(file_path)
    return image
    
def display(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for i in range(0,3):
    train = read_image(training_pictures[i])
    test = read_image(test_pictures[i])
    #print(f"Displaying image {i+1}: {training_pictures[i]}")
    display(test)