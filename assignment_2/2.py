import cv2

def crop(image, x_0, x_1, y_0, y_1):

    cropped_image = image[y_0:y_1, x_0:x_1]
    cv2.imwrite('cropped_image.jpg', cropped_image)
    print("Image saved as 'cropped_image.jpg'.")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        height, width = image.shape[:2]

        # crop 80 px from top & left, 130 px from bottom & right
        x_0 = 80
        x_1 = width - 130
        y_0 = 80
        y_1 = height - 130

        crop(image, x_0, x_1, y_0, y_1)
