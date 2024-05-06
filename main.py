# Import necessary functions and modules
from function import screenshot, findWords, copyPasteText
from playsound import playsound
import os, keyboard, time, pyautogui, re

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
    if len(text) != 0 and not bool(re.search(r'[^a-zA-Z]', text)):
        wordList = findWords.searchWords(text)
        
        # Copy and paste the selected word
        copyPasteText.typeWord(wordList, usedWords, urgent=False)
    else:
        # If no text extracted, play a buzzer sound
        playsound(r"static\buzzer-or-wrong-answer-20582.mp3")
        
        # Save letters and type the word
        text, urgent = copyPasteText.saveLetters()
        wordList = findWords.searchWords(text)
        time.sleep(0.5)
        
        # Click at coordinates (803, 1003) assuming it's a specific location
        pyautogui.click(803, 1003)
        
        # Type the word
        copyPasteText.typeWord(wordList, usedWords, urgent)

if __name__ == "__main__":
    # Initialize list to store used words
    usedWords = []
    
    # Continuously wait for the Shift key press and execute the main function
    while True:
        print("running")
        keyboard.wait("shift")
        main()