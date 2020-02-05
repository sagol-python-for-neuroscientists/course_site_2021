# encoding: utf-8
cimport cython
cimport numpy as np
import numpy as np


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef np.ndarray[np.float64_t, ndim=1] filter_larger_cython(np.ndarray[np.float64_t, ndim=1] rands):
    cdef np.ndarray[np.float64_t, ndim=1] result = np.zeros_like(rands)
    cdef unsigned long idx
    cdef unsigned long length = len(rands)
    cdef float thresh = 0.5
    cdef int last_idx = 0

    for idx in range(length):
        if rands[idx] <= 0.5:
            result[last_idx] = rands[idx]
            last_idx += 1
    return result[:last_idx]
