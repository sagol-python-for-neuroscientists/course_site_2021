"""
__author__ = Hagai Har-Gil
"""
from Classes.tests_demo.intadd_proj.intadd.intadd import intadd
import pytest


class TestIntadd:
    """ Grouped tests for intadd function """

    def test_basic_addition(self):
        assert intadd(2, 4) == 6

    def test_negative_inp1(self):
        with pytest.raises(TypeError):
            intadd(-1, 1)

    def test_negative_inp2(self):
        with pytest.raises(TypeError):
            intadd(1, -1)

    # Showing how "parametrize" works
    @pytest.mark.parametrize('inp, res', [((1, 2), 3),
                                          ((4, 5), 9)])
    def test_valid_inp(self, inp, res):
        assert intadd(inp[0], inp[1]) == res

    @pytest.mark.parametrize('inp', [(1., 2), (2, 1.)])
    def test_float_inp(self, inp):
        with pytest.raises(TypeError):
            intadd(inp[0], inp[1])
