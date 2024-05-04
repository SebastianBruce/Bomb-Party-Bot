import pyautogui, random, os, keyboard

def typeWord(wordList, usedWords, urgent):
    # Initialize a placeholder for the word
    word = "_"

    # Get the directory path of the current script
    scriptDir = os.path.dirname(__file__)
    
    # Construct the path to keys.txt relative to the current script
    keyPath = os.path.join(scriptDir, '..', 'static', 'keys.txt')

    # Open keys.txt and extract keys into a list
    with open(keyPath, 'r') as file:
        keys = [key.strip() for key in file]

    # Check if there's a word list and it's not empty
    if wordList is not None and len(wordList) != 0:
        # Loop until a new word is generated that hasn't been used before
        while word not in usedWords:
            if urgent:
                # If urgent mode is enabled and there are at least 3 words in the list,
                # select a random word from the first 3, otherwise select the first word.
                if len(wordList) >= 3:
                    word = wordList[random.randint(0, 2)]
                else:
                    word = wordList[0]
            else:
                # If urgent mode is disabled, select a random word from the list
                word = wordList[random.randint(0, len(wordList) - 1)]

            # Add the selected word to the list of used words
            usedWords.append(word)

        # Type each character of the word with random intervals
        for char in word:
            interval = 0.02 + random.uniform(-0.02, 0.01)
            pyautogui.typewrite(char, interval=interval)

            # Introduce occasional errors by typing adjacent keys
            if random.randint(0, 20) == 0:
                index = keys.index(char)
                pyautogui.typewrite(keys[random.randint(index - 2, index + 2)], interval=0.01)
                pyautogui.press('backspace')
            # Introduce occasional repeated characters
            elif random.randint(0, 100) == 0:
                index = keys.index(char)
                for i in range(3):
                    pyautogui.typewrite(keys[random.randint(index - 3, index + 3)], interval=0.01)
                for i in range(3):
                    pyautogui.press('backspace')

    # Press enter after typing the word
    pyautogui.press('enter')

    # Return the typed word
    return word

def saveLetters():
    # Define a string to store the keystrokes
    keystrokes = ""
    tracking = True
    urgent = True

    # Define a function to handle keyboard events
    def onKeyEvent(event):
        nonlocal keystrokes, tracking
        # If the enter key is pressed, stop tracking keystrokes
        if event.name == 'enter':
            tracking = False
            keyboard.unhook_all()
        # If the backspace key is pressed, remove the last character from keystrokes
        elif event.name == 'backspace':
            keystrokes = keystrokes[:-1]
        else:
            # Append the key to the keystrokes string
            keystrokes += event.name
            # Print the current content of keystrokes
            print(keystrokes)

    # Hook the keyboard events to the onKeyEvent function
    keyboard.on_press(onKeyEvent)

    # Loop until enter key is pressed
    while tracking:
        pass

    # Return the collected keystrokes and urgency flag
    return keystrokes, urgent
