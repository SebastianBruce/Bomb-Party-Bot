import cv2, pytesseract, pyautogui, os
import numpy as np
from PIL import Image

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), "Tesseract-OCR", "tesseract.exe")

# Define the folder path for saving screenshots
folderPath = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

def captureScreen():
    # Define the region to capture (x, y, width, height)
    region = (779, 543, 835-779, 608-543)

    # Capture the screen with the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Convert PIL image to OpenCV format
    screenshot_cv2 = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define the scaling factor for resizing the image
    scale_factor = 4  # Adjust this factor as needed

    # Resize the image using bicubic interpolation
    resized_image = cv2.resize(screenshot_cv2, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # Convert the resized image back to PIL format
    resized_image_pil = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    # Save the resized image
    resized_image_pil.save(os.path.join(folderPath, "word-bomb.jpg"))

    # Return the path to the saved screenshot
    path = os.path.join(folderPath, "word-bomb.jpg")
    return path

def preprocessImage(image, path):
    # Read the image
    image = cv2.imread(image)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image
    cv2.imwrite(path, gray)
    
    # Return the grayscale image
    return gray

def extractText(image):
    # Use Tesseract OCR to extract text from the image
    return pytesseract.image_to_string(image).strip()
