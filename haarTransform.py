from PIL import Image
import numpy as np

#works for pics with a size of multiple of 8

def haar(image, n):
    width, height = img.size

    pixels = np.asarray(image)

    h1 = [
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, -1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, -1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, -1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, -1]
        ]

    h1 = np.divide(h1, 2)

    h2 = [
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, -1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1]
        ]
    h2 = np.divide(h2, 2)

    h3 = [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, -1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1]
        ]
    h3 = np.divide(h3, 2)

    # set matrix H:
    if n == 1:
        h = h1
        addedVal = 4
    elif n == 2:
        h = np.dot(h1, h2)
        addedVal = 2
    elif n == 3:
        h = np.dot(h1, h2)
        h = np.dot(h, h3)
        addedVal = 1

    #the result matrix
    res = [[0]*int(width/(2**n))]*int(height/(2**n))
    res = np.array(res)

    i_res = 0
    j_res = 0

    for i in range(0, width, 8):
        j_res = 0
        for j in range(0, height, 8):
            pixels8 = pixels[i:i + 8, j: j + 8]
            pixels8 = np.dot(h.T, pixels8)
            pixels8 = np.dot(pixels8, h)

            res[i_res: i_res+addedVal, j_res: j_res + addedVal] = pixels8[0:addedVal, 0:addedVal]
            j_res += addedVal

        i_res += addedVal

    resImg = Image.fromarray(res)
    resImg.show()
    print(resImg.size)

# Read image
img = Image.open('batman.jfif')

img = img.convert('L')
print(img.size)
img.show()

haar(img, 1)
haar(img, 2)
haar(img, 3)
