import cv2, pytesseract, pyautogui, os
import numpy as np
from PIL import Image

#361, 364
#1250, 795

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), "Tesseract-OCR", "tesseract.exe")

folderPath = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

def captureScreen():
    # Define the region to capture
    region = (779, 543, 835-779, 608-543)

    # Capture the screen with the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Convert PIL image to OpenCV format
    screenshot_cv2 = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define the scaling factor
    scale_factor = 4  # Adjust this factor as needed

    # Resize the image using bicubic interpolation
    resized_image = cv2.resize(screenshot_cv2, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # Convert the resized image back to PIL format
    resized_image_pil = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    # Save the resized image
    resized_image_pil.save(os.path.join(folderPath, "word-bomb.jpg"))

    path = os.path.join(folderPath, "word-bomb.jpg")
    return path

def preprocessImage(image, path):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, gray)
    return gray

def extractText(image):
    # Use Tesseract OCR to extract text
    return pytesseract.image_to_string(image).strip()

