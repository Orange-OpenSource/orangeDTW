"""Python 2 or 3 example for DTW"""


# Copyright © 2019 Orange – All rights reserved

# before executing compile DTW.FOR using f2py or f2py3

import numpy as np
import dtw

def cdist_dtw(mat1, mat2):
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return dtw.dtw(adim1=mat1.shape[1], bdim1=mat2.shape[1], adim2=mat1.shape[0], bdim2=mat2.shape[0],
                   a=mat1, b=mat2)

a = np.random.random([3, 1000])
b = np.random.random([2, 1000])
print('the dtw distance of the sequences are', str(cdist_dtw(a,b)).replace('\n',''))
