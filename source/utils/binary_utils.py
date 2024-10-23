import numpy as np


class BinaryUtils:
    @staticmethod
    def get_binary_length(start_interval: float, end_interval: float, precision: int) -> int:
        """
        Calculates the binary length required to represent a number in a given range with specified precision.

        :param start_interval: Start of the interval.
        :param end_interval: End of the interval.
        :param precision: Number of decimal places.
        :return: Rounded up binary length.
        """
        number_of_intervals = (end_interval - start_interval) * pow(10, precision)
        binary_length = np.log2(number_of_intervals)
        rounded_up_binary_length = np.ceil(binary_length)
        return int(rounded_up_binary_length)

    @staticmethod
    def decode_number(binary_array: np.ndarray) -> int:
        """
        Decodes a binary array to a decimal number.

        :param binary_array: Binary array.
        :return: Decoded decimal number.
        """
        return np.sum(binary_array * (2 ** np.arange(binary_array.size)[::-1]))
