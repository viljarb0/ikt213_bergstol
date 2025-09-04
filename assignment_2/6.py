import cv2

def hsv(image):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite('hsv_image.jpg', hsv_image)
    print("Image saved as 'hsv_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        hsv(image)
