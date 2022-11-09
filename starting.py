import numpy as np
import h5py
import pandas as pd
f = h5py.File('mouse_matrix_v11.h5', "r")
data=f.keys()
for key in f.keys():
    print(key)
for key in f['meta'].keys():
    print(key)
for key in f['meta']['samples'].keys():
    print(key)
for elem in f['meta']['samples']['data_processing']:
    print(elem)
