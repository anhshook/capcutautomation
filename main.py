import pyautogui
import time
import subprocess
import os

# Disable PyAutoGUI fail-safe (use with caution)
pyautogui.FAILSAFE = False

# Log positions to avoid repeating incorrect positions
positions = {
    "text_icon": {"x": 160, "y": 80},
    "auto_captions_button": {"x": 45, "y": 320},  # Moved significantly further up
    "generate_button": {"x": 690, "y": 610}
}


def log_position(action):
    x, y = pyautogui.position()
    positions[action] = {"x": x, "y": y}
    print(f"{action} position: x={x}, y={y}")


def click_position(action_name):
    x, y = positions[action_name]["x"], positions[action_name]["y"]
    print(f"Clicking on {action_name} at position ({x}, {y})")
    pyautogui.click(x=x, y=y)
    time.sleep(2)


def open_capcut():
    print("Opening CapCut...")
    subprocess.Popen(["/Applications/CapCut.app/Contents/MacOS/CapCut"], stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)
    time.sleep(10)  # Wait for CapCut to open


def bring_capcut_to_foreground():
    print("Bringing CapCut to the foreground...")
    os.system('''/usr/bin/osascript -e 'tell application "CapCut" to activate' ''')
    time.sleep(2)


def create_new_project():
    print("Creating a new project in CapCut...")
    bring_capcut_to_foreground()
    pyautogui.keyDown('command')
    pyautogui.press('n')
    pyautogui.keyUp('command')
    print("New project creation command sent.")
    time.sleep(5)  # Wait to ensure the new project is created


def import_clips(directory):
    print(f"Importing clips from directory: {directory}")
    bring_capcut_to_foreground()
    pyautogui.hotkey('command', 'i')  # Open the import dialog
    time.sleep(2)
    pyautogui.hotkey('command', 'shift', 'g')  # Open "Go to Folder" dialog
    time.sleep(1)
    pyautogui.typewrite(directory)  # Type the path of the directory
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('command', 'a')  # Select all files
    time.sleep(1)
    pyautogui.press('enter')  # Confirm the selection
    time.sleep(5)  # Wait to ensure the files are imported


def drag_all_clips_to_timeline():
    print("Dragging all clips to the timeline")
    bring_capcut_to_foreground()

    # Ensure the clips are selected in CapCut
    pyautogui.click(x=190, y=250)  # Adjust to where the clips are located
    time.sleep(1)

    # Drag the files to the timeline
    pyautogui.mouseDown(button='left', x=190, y=250)  # Adjust coordinates to the initial clip location
    time.sleep(1)
    pyautogui.moveTo(300, y=800, duration=2)  # Adjust to the timeline area in CapCut
    pyautogui.mouseUp(button='left')
    time.sleep(5)  # Wait to ensure the files are moved


def add_auto_captions():
    print("Starting the process to add auto captions...")

    try:
        # Click on "Text" menu (TI icon)
        print("Clicking on the 'Text' icon...")
        click_position("text_icon")
        log_position("text_icon")

        # Click on "Auto captions"
        print("Clicking on the 'Auto captions' button...")
        click_position("auto_captions_button")
        log_position("auto_captions_button")

        # Click "Generate" button
        print("Clicking on the 'Generate' button...")
        click_position("generate_button")
        log_position("generate_button")
        time.sleep(5)  # Wait to ensure the captions are generated

        print("Finished adding auto captions.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    open_capcut()
    create_new_project()
    import_clips("/Users/anh/Downloads/Capcut videos/Stealth 600 FR")
    drag_all_clips_to_timeline()
    add_auto_captions()

