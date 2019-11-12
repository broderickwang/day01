import os
from urllib.request import urlretrieve

os.makedirs('./img/',exist_ok=True)

IMAGE_URL="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

urlretrieve(IMAGE_URL,"./img/image1.png")