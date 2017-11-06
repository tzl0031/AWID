import tensorflow as tf
import numpy as np
import os
import pickle
import gzip
import urllib.request
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.models import load_mode


def load(filename, num_data):
    df = pd.read_csv(filename, header=None)
    data = df[0:42]





def PCA()


class AWID:
    def __init__(self):
        train_data = extract_data()