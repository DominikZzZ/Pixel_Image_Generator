
import random
from PIL import Image


# Returns a 16x16 grid of random values (0 or 1) with a frequency of "freq" (0.25 in this case)
def create_a_grid():
    return [[random.randint(0, 1) if random.random() < freq else 1 for _ in range(grid_size)] for _ in range(grid_size)]

# Set the pixel data
def set_pixels_data():
    pixels = [
        (0, 0, 0) if grid[i // int(pixel_size)][j // int(pixel_size)] == 1 else (255, 255, 255) 
        for i in range(img_h)
        for j in range(img_w)
    ]
    img.putdata(pixels)


img_res = img_w, img_h = 512, 512

# You can enter any number between 0 and 1
freq: float = 0.25

grid_size = 16
grid = create_a_grid()

pixel_size = 32


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
