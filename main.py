import cv2
import pytesseract
import pyautogui
import numpy as np
import time, os

#361, 364
#1250, 795

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), "Tesseract-OCR", "tesseract.exe")

folderPath = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

def captureScreen():
    screenshot = pyautogui.screenshot(region=(781, 550, 833-781, 615-550))
    screenshot.save(os.path.join(folderPath, "word-bomb.jpg"))
    path = os.path.join(folderPath, "word-bomb.jpg")
    return path

def preprocessImage(image, path):
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, gray)
    return gray

def extractText(image):
    # Use Tesseract OCR to extract text
    return pytesseract.image_to_string(image)

def main():
    while True:
        previous_text = ""
        # Capture the screen
        screenshotPath = captureScreen()
        processedPath = os.path.join(folderPath, "word-bomb-processed.jpg")
        preprocessImage(screenshotPath, processedPath)
        text = extractText(processedPath)
        print(text)
        time.sleep(1)

if __name__ == "__main__":
    main()

