
import cv2
import numpy as np  
from matplotlib import pyplot as plt

def template_match(image, template):
    
    # Read the main image and template
    img = cv2.imread(image)
    template = cv2.imread(template)
    
    # Convert both images to grayscale (required for template matching)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Get template dimensions
    w, h = template_gray.shape[::-1]
    
    # Perform template matching using cv2.TM_CCOEFF_NORMED method
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    
    # Set threshold to 0.9 as specified
    threshold = 0.9
    
    # Find locations where matching exceeds threshold
    loc = np.where(res >= threshold)
    
    # Draw red rectangles around matched areas
    for pt in zip(*loc[::-1]):  # Switch coordinates because loc gives (y,x)
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)  # Red color (BGR format)
    
    # Save the result image
    cv2.imwrite("template_match_result.jpg", img)
    
    # Display information about matches found
    matches_found = len(loc[0])
    print(f"Number of matches found with threshold {threshold}: {matches_found}")

def sobel_edge_detection(image):
    # Convert to graycsale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    #sobel_edges = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1) # Combined X and Y Sobel Edge Detection
    sobel_edges =(255*cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1) ).clip(0,255).astype(np.uint8)  # Combined X and Y Sobel Edge Detection
    # Save the result image
    cv2.imwrite("sobel_edges.png", sobel_edges)


def canny_edge_detection(image, threshold_1, threshold_2):
    # Convert to graycsale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    # Canny Edge Detection
    canny_edges = cv2.Canny(image=img_blur, threshold1=threshold_1, threshold2=threshold_2) # Canny Edge Detection
    # Save the result image
    cv2.imwrite("canny_edges.png", canny_edges)


def resize(image, scale_factor: int, up_or_down: str):
    cv2.imwrite("resized.png", resized_image)
    

# Read the original image
image = cv2.imread('lambo.png') 
sobel_edge_detection(image)
canny_edge_detection(image, 50, 50)
template_match("shapes-1.png","shapes_template.jpg")