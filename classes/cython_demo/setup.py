from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Cython Demo",
    ext_modules=cythonize('primes_cython.pyx'),  # Python code file with primes_python_compiled() function
    zip_safe=False,
)
