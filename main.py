from function import screenshot, findWords, copyPasteText
from playsound import playsound
import os, keyboard, time, pyautogui
def main():
    # Capture the screen
    screenshotPath = screenshot.captureScreen()
    
    # Define the path for the processed screenshot
    processedPath = os.path.join(screenshot.folderPath, "word-bomb-processed.jpg")
    
    # Preprocess the captured screenshot
    screenshot.preprocessImage(screenshotPath, processedPath)
    
    # Extract text from the processed image
    text = screenshot.extractText(processedPath)
    print(text)
    # Search for words containing the extracted text
    if len(text) != 0:
        wordList = findWords.searchWords(text)
        # Copy and paste the selected word
        copyPasteText.typeWord(wordList, urgent = False)
    else:
        playsound(r"static\buzzer-or-wrong-answer-20582.mp3")
        text, urgent = copyPasteText.saveLetters()
        wordList = findWords.searchWords(text)
        time.sleep(0.5)
        pyautogui.click(803, 1003)
        copyPasteText.typeWord(wordList, urgent)

if __name__ == "__main__":
    # Continuously wait for the F4 key press and execute the main function
    while True:
        print("running")
        keyboard.wait("shift")
        main()
