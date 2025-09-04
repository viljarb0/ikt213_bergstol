import cv2
import numpy as np

def copy(image, emptyPictureArray):

    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                emptyPictureArray[y, x, c] = image[y, x, c]

    cv2.imwrite('copied_image.jpg', emptyPictureArray)
    print("Image saved as 'copied_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        height, width, channels = image.shape
        emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
        copy(image, emptyPictureArray)
