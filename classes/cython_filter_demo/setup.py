"""
__author__ = Hagai Har-Gil
"""
from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize('filter_array.pyx',
                          annotate=True),
    include_dirs=[np.get_include()]
)