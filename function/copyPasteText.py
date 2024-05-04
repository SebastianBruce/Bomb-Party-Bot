import pyperclip, pyautogui, keyboard

def copyPaste(wordList):
    if wordList != 0:
        # Copy the last word in the word list to the clipboard
        word = wordList[-1]
        
        # Simulate 'Ctrl + V' to paste the word
        pyautogui.typewrite(word, interval=0.05)
