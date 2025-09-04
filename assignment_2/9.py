import cv2

def rotation(image, rotation_angle):

    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    else:
        print("Invalid angle. Use 90 or 180.")
        return

    cv2.imwrite('rotated_image.jpg', rotated_image)
    print("Image saved as 'rotated_image.jpg'.")
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Image not found.")
    else:
        rotation(image, rotation_angle=90)  # degrees
