import pyautogui, random, os, keyboard

def typeWord(wordList, urgent):
    # Get the directory path of the current script
    scriptDir = os.path.dirname(__file__)
    
    # Construct the path to words.txt relative to the current script
    keyPath = os.path.join(scriptDir, '..', 'static', 'keys.txt')

    # Open words.txt and extract words into a list
    with open(keyPath, 'r') as file:
        keys = [key.strip() for key in file]

    if wordList is not None and wordList != 0:
        if urgent:
            if len(wordList) >= 3:
                word = wordList[random.randint(0, 2)]
            else:
                word = wordList[0]
        else:
            # Copy the last word in the word list to the clipboard
            word = wordList[random.randint(0, len(wordList) - 1)]

        for char in word:
            interval = 0.02 + random.uniform(-0.02, 0.01)
            pyautogui.typewrite(char, interval=interval)

            if random.randint(0, 20) == 0:
                index = keys.index(char)

                pyautogui.typewrite(keys[random.randint(index - 2, index + 2)], interval=0.01)
                pyautogui.press('backspace')
            elif random.randint(0, 100) == 0:
                key = random.randint(0, len(keys) - 1)
                index = keys.index(char)
                for i in range(3):
                    pyautogui.typewrite(keys[random.randint(index - 4, index + 4)], interval=0.01)
                for i in range(3):
                    pyautogui.press('backspace')
    pyautogui.press('enter')

def saveLetters():
    # Define a string to store the keystrokes
    keystrokes = ""
    tracking = True
    urgent = True

    def onKeyEvent(event):
        nonlocal keystrokes, tracking
        if event.name == 'enter':
            tracking = False
            keyboard.unhook_all()
        elif event.name == 'backspace':
            keystrokes = keystrokes[:-1]
        else:
            # Append the key to the keystrokes string
            keystrokes += event.name
            print(keystrokes)

    keyboard.on_press(onKeyEvent)

    # Loop until enter key is pressed
    while tracking:
        pass

    return keystrokes, urgent