import pyperclip, pyautogui, keyboard

def copyPaste(wordList):
    # Copy the last word in the word list to the clipboard
    pyperclip.copy(wordList[-1])
    
    # Simulate 'Ctrl + V' to paste the word
    pyautogui.hotkey('ctrl', 'v')
