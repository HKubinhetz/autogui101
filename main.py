# --------------------- IMPORTS  ---------------------
import pyautogui

# --------------------- VARIABLES --------------------

last30 = [(0, 0)]*30

# -------------------- MAIN LOOP  --------------------
while True:
    # Gets starting position
    x0, y0 = pyautogui.position()
    starting_position = (x0, y0)
    # print(f"Current Mouse Position: {starting_position}")

    # Appends position to the end of the list and removes first element
    last30.append(starting_position)
    last30.pop(0)
    # print(last30)

    # Gets end position
    pyautogui.sleep(1)
    end_position = pyautogui.position()

    if all(position == starting_position for position in last30):
        print("AFK!")
        pyautogui.click()
        pyautogui.sleep(1)

    else:
        print("Not AFK!")







