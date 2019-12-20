EFFICIENT DTW FOR PYTHON 2 AND 3

Copyright (C) 2019 Jerome GALTIER Orange Labs

# INSTALLATION

The program f2py or f2py3 should already be installed, along with the fortran compiler (gfortran for instance).

Compile the python library with:

f2py -m dtw -c DTW.FOR

or

f2py3 -m dtw -c DTW.FOR

# USE UNDER PYTHON 2 OR 3

The library should be imported using

import dtw

then the library is called by the syntax dtw.dtw(adim1=adim1 bdim1=bdim1, adim2=adim2, bdim2=bdim2, a=a, b=b)

a and b are numpy arrays of respective dimensions [adim2, adim1] and [bdim2, bdim1].
The procedures returns an array of reals of dimension [adim2, bdim2].

