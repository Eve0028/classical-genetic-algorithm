import random
from typing import List

class RandomGenerator:

    @staticmethod
    def generate_random_list(number_of_elements: int, low_boundary: int, high_boundary: int) -> List[int]:
        range_list = list(range(low_boundary, high_boundary))
        sampled_numbers = random.sample(range_list, number_of_elements)
        return sampled_numbers

