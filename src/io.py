# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:21:04 2026

@author: Kwihoon
"""

import pandas as pd
import numpy as np


def load_idf_table(path="input/IDF_coef.txt"):
    return pd.read_table(path)


def load_variable(var, path="input/variable.txt"):
    variable = pd.read_table(path, sep="\t", thousands=",")
    return variable[var]


def load_volume(var):
    path = f"input/volume_Flooding_{var.upper()}.txt"
    vol = pd.read_table(path, sep="\t", thousands=",")
    vol = vol.drop(['번호'], axis=1)
    return np.array(vol)