import cv2
import numpy as np

def hue_shifted(image, emptyPictureArray, hue):

    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                new_value = image[y, x, c] + hue
                # Clip the value to stay within [0, 255]
                emptyPictureArray[y, x, c] = np.clip(new_value, 0, 255)

    cv2.imwrite('hue_shifted_image.jpg', emptyPictureArray)
    print("Image saved as 'hue_shifted_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        height, width, channels = image.shape
        emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
        hue_shifted(image, emptyPictureArray, hue=50)
