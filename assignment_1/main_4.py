

import cv2

def show_image(image):
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def print_image_information(image):
    # Get image dimensions
    height, width, channels = image.shape

    # Print image info
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    print("Size:", image.size)
    print("Data type:", image.dtype)
image = cv2.imread("lena-1.png")
print_image_information(image)
show_image(image)