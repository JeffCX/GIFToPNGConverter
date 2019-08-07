from PIL import Image
import os

gif_name = 'giphy.gif'
image_folder = "img/"
image_name = "image"

def convertGIFToPNGs(gif_name, image_folder, image_name, extension=".png"):
    if not os.path.isdir(image_folder):
        os.mkdir(image_folder)
    img = Image.open(gif_name)
    index = 1
    for frame in range(0, img.n_frames):
        img.seek(frame)
        saved_image_name = os.path.join(image_folder, image_name + str(index) + ".png")
        index += 1
        img.save(saved_image_name, 'png' , optimize = True, quality = 100)
        index += 1

convertGIFToPNGs(gif_name, image_folder, image_name)