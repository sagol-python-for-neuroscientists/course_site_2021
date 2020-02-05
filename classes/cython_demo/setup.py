"""
__author__ = Hagai Har-Gil
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('primes_cython.pyx')  # Python code file with primes_python_compiled() function
)