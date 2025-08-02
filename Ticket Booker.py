import subprocess
import time
import pyautogui
import traceback


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


origin="BAPUDM MOTIHARI - BMKI"
destination="ANAND VIHAR TRM - ANVT (NEW DELHI)"
journeyDate="1/09/2025"
journetClass="g" #Always use small letter
trainNumber="12555"

def findModifySearch(image_path, confidence=0.8):
    try:
        found = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if found:
            return found
    except pyautogui.ImageNotFoundException:
        pass
    return None

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
    pyautogui.press("enter")
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
                return None
        except pyautogui.ImageNotFoundException:
            print("Loader not found on the screen. Proceeding to find train...")
            return None
        time.sleep(0.5)

def select_Train(image_path, confidence=0.8):
    try:
        box = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if not box:
            print("Train name not found.")
            return None

        top_left = (box.left, box.top)
        pyautogui.click(top_left)
        region = (box.left, box.top, int(1131.2), int(400.6))
        print(f"Defined region: {region}")

        # Move mouse to bottom-left of region
        # bottom_left = (box.left, box.top + int(400.6) - 1)
        # pyautogui.moveTo(bottom_left)
        # print(f"Moved mouse to bottom-left of region: {bottom_left}")
        # time.sleep(2)

        # Try locating and clicking B_SL twice
        for attempt in range(2):
            B_Class = pyautogui.locateOnScreen('Images/ClassImage/B/B_SL.png', region=region, confidence=confidence)
            if B_Class:
                pyautogui.click(B_Class)
                print(f"'B_SL' clicked on attempt {attempt + 1}")
                break
            else:
                print(f"'B_SL' not found on attempt {attempt + 1}")
        else:
            print("B_SL not found after 2 attempts.")
            return top_left

        waitForLoaderToFinish("Images/LoadingImage.png")

        pyautogui.click(box.left + 100, box.top + 200)
        print(f"Clicked fixed coordinate at ({box.left + 100}, {box.top + 200})")

        time.sleep(.5) 
        # Try to find and click BookNow
        while True:
            try:
                BookNow = pyautogui.locateOnScreen('Images/BookNow.png', region=region, confidence=confidence)
            except pyautogui.ImageNotFoundException:
                BookNow = None
            if BookNow:
                pyautogui.click(BookNow)
                print("Clicked 'BookNow' button.")
                return top_left
            # If BookNow not found, click, find S_SL, click, coordinate click, retry BookNow
            try:
                S_SL = pyautogui.locateOnScreen('Images/ClassImage/S/S_SL.png', region=region, confidence=confidence)
            except pyautogui.ImageNotFoundException:
                S_SL = None
            if S_SL:
                pyautogui.click(S_SL)
                print("Clicked 'S_SL' button.")
                waitForLoaderToFinish("Images/LoadingImage.png")
                pyautogui.click(box.left + 100, box.top + 200)
                print(f"Clicked fixed coordinate again at ({box.left + 100}, {box.top + 200})")
                time.sleep(.5)
                # Loop will retry BookNow
            else:
                print("S_SL not found. Stopping loop.")
                break
        return top_left

    except Exception:
        traceback.print_exc()
        return None


def run():
    ensure_chrome_active()
    time.sleep(1)
    fillJourneyDetails("Images/BookTicketAtStationFilling.png")
    waitForLoaderToFinish("Images/LoadingImage.png")
    findModifySearch("Images\ModifySearch.png")
    find_Train()
    select_Train("Images/SaptKranti.png")

# run()






