import os
from PIL import Image
import concurrent.futures

os.chdir("----raw pictures' directory path----")
destination = "----processed pictures' directory path----"


def process_image(img_name):
    image = Image.open(img_name)

    # next 3 lines strip exif
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    image_without_exif.save(os.path.join(destination, img_name))
    os.remove(img_name)


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, os.listdir())
    print("Job Done!")
