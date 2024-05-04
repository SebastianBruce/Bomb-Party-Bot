import pyperclip, pyautogui, keyboard

def copyPaste(wordList):
    pyperclip.copy(wordList[-1])
    pyautogui.hotkey('ctrl', 'v')