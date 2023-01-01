
import random
from PIL import Image


# Returns a grid (8x8 in this case) of random values (0 or 1) with a frequency of "freq" (0.35 in this case)
def create_a_grid():
    return [[random.randint(0, 1) if random.random() < freq else 1 for _ in range(grid_size)] for _ in range(grid_size)]

# Set the pixel data
def set_pixels_data():
    pixels = [
        (0, 0, 0) if grid[i][j] == 1 else (255, 255, 255) 
        for i in range(img_size)
        for j in range(img_size)
    ]
    img.putdata(pixels)


# Frequency (freq) settings
# You can enter any number between 0 and 1
freq: float = 0.35

# Image (img) settings
img_size = 8
img_res = (img_size, img_size)

# Grid settings
# "grid_size" shouldn't be smaller or bigger than "img_size"
grid_size = img_size
grid = create_a_grid()

# Pixel settings
pixel_size = img_size / grid_size


# main
if __name__ == "__main__":
    # Create a new image object with the given size (512x512 in this case)
    img = Image.new("RGB", img_res)

    set_pixels_data()

    # Show the image
    img.show()

    # Save the image
    # If you want to save this image you can uncomment "#img.save("img.png")"
    #img.save("img.png")
