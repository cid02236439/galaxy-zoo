#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 16:00:02 2025

@author: praneshdara
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
import pandas as pd
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
    image = read_image(training_pictures[i])
    params = training_solutions.iloc[i]
    id = int(training_pictures[i].split('/')[-1].split('.')[0])
    id2 = int(params['GalaxyID'])
    if not id == id2:
        raise ValueError(f"ID mismatch: {id} != {id2}")
    
