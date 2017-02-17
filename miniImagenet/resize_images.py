from PIL import Image
import glob

image_path = 'images/'

all_images = glob.glob(image_path + '*')

i = 0

for image_file in all_images:
    im = Image.open(image_file)
    im.resize((84,84), resample=Image.LANCZOS)
    im.save(image_file)
    i += 1

    if i % 200 == 0:
        print i

