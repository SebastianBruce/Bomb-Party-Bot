from function import screenshot, findWords, copyPasteText
import os, time, keyboard

def main():
    # Capture the screen
    screenshotPath = screenshot.captureScreen()
    
    # Define the path for the processed screenshot
    processedPath = os.path.join(screenshot.folderPath, "word-bomb-processed.jpg")
    
    # Preprocess the captured screenshot
    screenshot.preprocessImage(screenshotPath, processedPath)
    
    # Extract text from the processed image
    text = screenshot.extractText(processedPath)
    
    # Search for words containing the extracted text
    wordList = findWords.searchWords(text)
    
    # Copy and paste the selected word
    copyPasteText.copyPaste(wordList)

if __name__ == "__main__":
    print("running")
    
    # Continuously wait for the F4 key press and execute the main function
    while True:
        keyboard.wait("f4")
        main()
