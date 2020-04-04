import os
from shutil import move
dir_src = r"O:\02_images_rotated\images\charge_08\Compressed"
dir_dst = r"O:\02_images_rotated\images\charge_08"
for root, _, files in os.walk(dir_src):
    for file in files:
        if file.endswith('.jpg'):
            move(os.path.join(root, file), dir_dst)