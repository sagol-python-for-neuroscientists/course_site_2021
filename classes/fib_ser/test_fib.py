"""
__author__ = Hagai Har-Gil
"""
import pytest
import numpy as np

from fib_ser import *


class TestFib:
    fib = np.array([0, 1, 1, 2, 3, 5, 8, 13])
    primes = np.array([2, 3, 5, 7, 11, 13, 17, 19])

    @pytest.mark.parametrize('inp', [-1, 1., 'a', {},])
    def test_invalid_inp(self, inp):
        with pytest.raises(TypeError):
            CompareSeries(inp)

    def test_fib_valid(self):
        result = CompareSeries(4).gen_fib_arr()
        assert np.array_equal(result, self.fib[:4])

    def test_fib_single(self):
        result = CompareSeries(1).gen_fib_arr()
        assert np.array_equal(result, np.array([0]))

    def test_primes_valid(self):
        result = CompareSeries(6).gen_prime_arr()
        assert np.array_equal(result, self.primes[:6])

    def test_primes_single(self):
        result = CompareSeries(1).gen_prime_arr()
        assert result == np.array([2])

    # Integration tests
    def test_valid(self):
        result = CompareSeries(8).compare()
        assert np.array_equal((self.fib - self.primes), result)

    def test_zero(self):
        assert len(CompareSeries(0).compare()) == 0