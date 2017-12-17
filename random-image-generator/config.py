import os

config = {
    'random_org_url': os.getenv("RANDOM_ORG_URL", "https://www.random.org"),
    'random_org_endpoint': os.getenv("RANDOM_ORG_ENDPOINT", "/integers"),
    'img_rows': os.getenv("IMG_ROWS", 128),
    'img_cols': os.getenv("IMG_COLS", 128),
    'img_format': os.getenv("img_format", "RGB"),  # allowed modes are RGB and L (greyscale)
    'out_file_path': os.getenv("OUT_FILE_PATH", 'image.bmp'),
    'email': os.getenv("EMAIL", 'ronvohra@gmail.com')
}

random_params = {
    'num': 10000,
    'min': 0,
    'max': 255,
    'base': 10,
    'col': 1,
    'format': 'plain',
    'rnd': 'new'
}
