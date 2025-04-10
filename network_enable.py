import os
import sys
import pyautogui
import time

# === Check if script has already run ===
flag_path = os.path.expanduser("~\\AppData\\Local\\Temp\\network_script_ran.flag")
if os.path.exists(flag_path):
    sys.exit(0)  # Exit silently if flag file exists

# Create flag file to mark that the script has already run
with open(flag_path, 'w') as f:
    f.write("Already executed.")

# === Your network automation starts here ===

print("Starting in 3 seconds...")
time.sleep(3)

# Step 1: Open Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('ncpa.cpl', interval=0.1)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)

# Step 2: Select adapter and open Properties
pyautogui.press('right')
time.sleep(0.9)
pyautogui.press('left')
time.sleep(0.9)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab')
time.sleep(0.9)
pyautogui.press('enter')
time.sleep(2)

# Step 3: Navigate to Sharing tab
pyautogui.hotkey('shift', 'tab')
time.sleep(0.9)
pyautogui.hotkey('shift', 'tab')
time.sleep(0.9)
pyautogui.press('right')
time.sleep(1)

# Step 4: Enable ICS
pyautogui.press('tab')
time.sleep(0.9)
pyautogui.press('space')
time.sleep(0.9)

# Step 5: Press OK
pyautogui.press('tab')
time.sleep(0.9)
pyautogui.press('tab')
time.sleep(0.9)
pyautogui.press('tab')
time.sleep(0.9)
pyautogui.press('enter')
time.sleep(0.5)

# Step 6: Confirm additional dialog if it appears
pyautogui.press('enter')
time.sleep(0.5)

# Step 7: Close all windows
pyautogui.press('esc')
time.sleep(1)
pyautogui.press('esc')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')

