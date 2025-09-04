import cv2

def grayscale(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscale_image.jpg', gray_image)
    print("Image saved as 'grayscale_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        grayscale(image)
