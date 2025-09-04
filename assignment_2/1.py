
import cv2

def padding(image, border_width):

    padded_image = cv2.copyMakeBorder(
        image,
        top=border_width,
        bottom=border_width,
        left=border_width,
        right=border_width,
        borderType=cv2.BORDER_REFLECT
    )

    # Save the result
    cv2.imwrite('padded_image.jpg', padded_image)
    print("Image saved as 'padded_image.jpg'.")

# Example usage:
if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Failed to load the image.")
    else:
        padding(image, border_width=100)
