import pyautogui

# Function to continuously display mouse position
def display_mouse_position():
    try:
        while True:
            # Get and print the mouse coordinates
            x, y = pyautogui.position()
            print(f'X: {x}, Y: {y}')
    except KeyboardInterrupt:
        print('\nPosition tracking stopped.')

# Call the function to start displaying mouse position
display_mouse_position()