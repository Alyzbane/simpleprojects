from PIL import Image
import numpy as np

def pixels_2d(matrix):
    # Turning the image into pixelated arrays
    x, y = matrix.shape
    ascii_matrix = np.empty((x,y), dtype='<U1')
    for i in range(x):
        for j in range(y):
            pixel = matrix[i][j]
            avg = pixel.sum() // 3 # Average filter
            ascii_matrix[i][j] = pixel_ascii(avg)
    return ascii_matrix

# Assigning the pixel with the character
def pixel_ascii(pixel):
    ASCII_LEN = 255
    ascii_chars = "`^\\\",:;Il!i~+_-?][}{1)(|\\\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    # Inverted
    #ascii_chars = ascii_chars[::-1]
    # Average RGB
    index = max(0,int((pixel / ASCII_LEN) * len(ascii_chars) - 1))
    return ascii_chars[index]


# Turn the image into  B&W
img = Image.open("image.jpg").convert('L')
img = img.resize((400,400)) # Change the dimension as desired
pixels_matrix = np.array(img)
list_matrix = pixels_2d(pixels_matrix)

for row in list_matrix:
    # This will turn the image into fitted size in terminal
    print(''.join([char*3 for char in row]))

#print(pixel_ascii(0))


