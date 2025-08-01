import subprocess
import time
import pyautogui
import os


try:
    import pygetwindow as gw
except ImportError:
    gw = None

def ensure_chrome_active():
    """
    Checks if the current active window is Chrome. If not, opens Chrome and brings it to the front.
    Requires pygetwindow (pip install pygetwindow) and Chrome installed in PATH.
    """
    if gw is None:
        print("pygetwindow not installed. Please run: pip install pygetwindow")
        return
    win = gw.getActiveWindow()
    if win and 'chrome' in win.title.lower():
        print("Chrome is already the active window.")
        return
    # Try to find any open Chrome window
    chrome_windows = [w for w in gw.getAllWindows() if 'chrome' in w.title.lower()]
    if chrome_windows:
        chrome_windows[0].activate()
        print("Activated existing Chrome window.")
        return
    # If not found, open Chrome
    print("Opening Chrome...")
    subprocess.Popen('start chrome', shell=True)
    # Wait and try to activate
    time.sleep(2)
    chrome_windows = [w for w in gw.getAllWindows() if 'chrome' in w.title.lower()]
    if chrome_windows:
        chrome_windows[0].activate()
        print("Activated new Chrome window.")
    else:
        print("Could not activate Chrome window. Please check if Chrome is installed and in PATH.")


origin="LUCKNOW NR - LKO (LUCKNOW)"
destination="ANAND VIHAR TRM - ANVT (NEW DELHI)"
journeyDate="1/09/2025"
journetClass="g" #Always use small letter
trainNumber="12555"


def fillJourneyDetails(image_path, confidence=0.8):
    try:
        found = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if found:
            click_point = (found[0] - 200, found[1] + 90)
            pyautogui.click(click_point)

            pyautogui.write(origin)
            time.sleep(.2)
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.write(destination)
            time.sleep(.2)
            pyautogui.press("tab")
            pyautogui.write(journeyDate)
            time.sleep(.3)
            pyautogui.click(found[0] - 200, found[1] + 270)
            pyautogui.press(journetClass)
            pyautogui.click(0,500)
            time.sleep(.3)

            pyautogui.click(found[0] - 300, found[1] + 430)
            return found
    except pyautogui.ImageNotFoundException:
        pass
    return None

def find_Train():
    pyautogui.press("f3")
    pyautogui.write(trainNumber)
    # pyautogui.hotkey("ctrl","backspace")
    time.sleep(.3)
    pyautogui.click(1375,129)
    time.sleep(.5)
    pyautogui.click(0,500)
    
def waitForLoaderToFinish(image_path, confidence=0.8):
    while True:
        try:
            found = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if found:
                print("Loader Found Waiting...")
            else:
                print("Loader not found on the screen. Proceeding to find train...")
                find_Train()
                return None
        except pyautogui.ImageNotFoundException:
            print("Loader not found on the screen. Proceeding to find train...")
            find_Train()
            return None
        time.sleep(0.5)




ensure_chrome_active()
time.sleep(1)
fillJourneyDetails("Images/BookTicketAtStationFilling.png")
waitForLoaderToFinish("Images/loadingImage.png")



