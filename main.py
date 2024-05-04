from function import screenshot, findWords, copyPasteText
import os, time, keyboard

def main():
    # Capture the screen
    screenshotPath = screenshot.captureScreen()
    processedPath = os.path.join(screenshot.folderPath, "word-bomb-processed.jpg")
    screenshot.preprocessImage(screenshotPath, processedPath)
    text = screenshot.extractText(processedPath)
    wordList = findWords.searchWords(text)
    copyPasteText.copyPaste(wordList)

if __name__ == "__main__":
    print("running")
    while True:
        keyboard.wait("f4")  # Wait for key press instead of continuously checking
        main()  # Call main function when key is pressed