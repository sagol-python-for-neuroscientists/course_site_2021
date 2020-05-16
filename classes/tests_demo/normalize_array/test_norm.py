import numpy as np
import pytest

from norm import *


def test_norm_noop():
    inp = np.array([0., 0.5, 1.])
    result = normalize_array(inp)
    truth = inp.copy()
    np.testing.assert_array_equal(truth, result)


def test_norm_simple():
    inp = np.array([0., 1., 2.])
    result = normalize_array(inp)
    truth = np.array([0, 0.5, 1])
    np.testing.assert_array_almost_equal(truth, result)


def test_norm_simple_negative():
    inp = np.array([0., -1., -2.])
    result = normalize_array(inp)
    truth = np.array([1, 0.5, 0])
    np.testing.assert_array_almost_equal(truth, result)


@pytest.mark.parametrize('dt', [np.float32, np.float64])
def test_norm_dtype(dt):
    result = normalize_array(np.array([1., 2, 3], dtype=dt))
    assert result.dtype == dt


def test_norm_min_max():
    rand_arr = np.random.randint(0, 100, (100, 20))
    result = normalize_array(rand_arr)
    assert result.max() == 1.0
    assert result.min() == 0.0


shapes = [(1,), (10,), (1, 2), (5, 1), (20, 20, 30)]
@pytest.mark.parametrize('shape', shapes)
def test_norm_shapes(shape):
    rand_arr = np.random.randint(10, 20, shape)
    result = normalize_array(rand_arr)
    assert result.shape == shape


def test_norm_zero_is_max():
    arr = np.array([0, 0])
    result = normalize_array(arr)
    np.testing.assert_array_almost_equal(result, np.array([0, 0]))


def test_norm_identical_is_zeroed():
    arr = np.array([10, 10, 10.], dtype=np.float32)
    result = normalize_array(arr)
    np.testing.assert_array_almost_equal(result, np.array([0., 0., 0.,], dtype=np.float32))


def test_norm_with_nan():
    arr = np.array([np.nan, 1])
    result = normalize_array(arr)
    truth = np.array([0, 1.])
    np.testing.assert_array_almost_equal(result, truth)


def test_norm_all_nans():
    arr = np.array([[np.nan, np.nan]])
    result = normalize_array(arr)
    truth = np.array([[0., 0.]])
    np.testing.assert_array_almost_equal(result, truth)


def test_snapshots():
    fname = 'snapshot_05_2020.npz'
    data = np.load(fname)
    num_of_snaps = len(data) // 2
    for snap in range(1, num_of_snaps + 1):
        inp = data[f"input{snap}"]
        old_output = data[f"output{snap}"]
        new_output = normalize_array(inp)
        np.testing.assert_array_almost_equal(old_output, new_output)
