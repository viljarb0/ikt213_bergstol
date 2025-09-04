import cv2

def smoothing(image):

    smoothed_image = cv2.blur(image, ksize=(15, 15))
    cv2.imwrite('smoothed_image.jpg', smoothed_image)
    print("Image saved as 'smoothed_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        smoothing(image)
