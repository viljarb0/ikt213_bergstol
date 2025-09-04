import cv2

def resize(image, width, height):

    resized_image = cv2.resize(image, (width, height))
    cv2.imwrite('resized_image.jpg', resized_image)
    print("Image saved as 'resized_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        resize(image, width=200, height=200)
