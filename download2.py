import os
import requests

os.makedirs("./img/",exist_ok=True)

IMAGE_URL="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

r = requests.get(IMAGE_URL)
with open("./img/image2.png","wb") as f:
    f.write(r.content)
