import logging
import requests

from PIL import Image

from config import config, random_params


def get_pixel_count():
    num_rows, num_cols = int(config.get('img_rows')), int(config.get('img_cols'))
    format = config.get('img_format')

    if format not in ('RGB', 'L'):
        raise ValueError("config['img_format'] allows only 'RGB' and 'L' (greyscale values)")

    if format == 'RGB':
        num_channels = 3
    else:
        num_channels = 1

    return num_cols * num_rows * num_channels


def get_random_numbers(num=10000):

    url = config['random_org_url'] + config['random_org_endpoint']
    random_params['num'] = num
    headers = {'User-Agent': config.get('email')}

    resp = requests.get(url, params=random_params, headers=headers)

    if resp.ok:
        arr = [int(i) for i in resp.text.rstrip().split('\n')]
        return arr

    logging.error("Resp failed with status code %d: %s" % (resp.status_code, resp.text))
    return []


def group(lst, n):

    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)


def create_rgb_bitmap(arr):

    mat = list(group(list(arr), 3))  # create list of 3-tuples for RGB values

    assert(config.get('img_format') == 'RGB', "Image format must be set to 'RGB'")

    im = Image.new(config.get('img_format'), (config.get('img_rows'), config.get('img_cols')))
    im.putdata(mat)
    im.save(config.get('out_file_path'))

    im.show()
