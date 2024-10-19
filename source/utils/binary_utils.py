import numpy as np


class BinaryUtils:
    @staticmethod
    def get_binary_length(start_interval, end_interval, precision):
        number_of_intervals = (end_interval - start_interval) * pow(10, precision)
        binary_length = np.log2(number_of_intervals)
        rounded_up_binary_length = np.ceil(binary_length)
        return int(rounded_up_binary_length)

    @staticmethod
    def decode_number(binary_array):
        return np.sum(binary_array * (2 ** np.arange(binary_array.size)[::-1]))
