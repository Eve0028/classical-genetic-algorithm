import pytest
import numpy as np

from source.utils.binary_utils import BinaryUtils


def test_get_binary_length():
    binary_length = BinaryUtils.get_binary_length(-10, 10, 6)
    assert binary_length == 25


def test_decode_number():
    decoded_number = BinaryUtils.decode_number(np.array([1, 1, 0, 0, 0, 0, 0, 0, 1]))
    assert decoded_number == 385
    decoded_number = BinaryUtils.decode_number(np.array([1, 1, 1, 1, 1]))
    assert decoded_number == 31
