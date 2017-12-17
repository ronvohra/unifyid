import logging

from config import random_params
from generate_random_images import get_pixel_count, get_random_numbers, create_rgb_bitmap

logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s.%(funcName)s %(message)s', level=logging.INFO)


def main():

    num_pixels_remaining = get_pixel_count()
    req_limit = random_params.get('num')

    arr = []

    while num_pixels_remaining > req_limit:
        arr.extend(get_random_numbers(req_limit))
        num_pixels_remaining -= req_limit

    arr.extend(get_random_numbers(num_pixels_remaining))

    assert(get_pixel_count() == len(arr), "Random function did not source the correct number of integers")

    create_rgb_bitmap(arr)


if __name__ == '__main__':
    main()
