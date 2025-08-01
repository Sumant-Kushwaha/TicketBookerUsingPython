
import pyautogui
import time
from PIL import Image
import pytesseract

def find_ContinueButton(image_path, confidence=0.8):
    """
    Find an image on the screen using pyautogui.
    Returns the Box (left, top, width, height) if found, else None.
    """
    try:
        point = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if point:
            print(f"Image '{image_path}' found at: {point}")
            # Calculate screenshot region
            x = int(point[0]) + 446
            y = int(point[1]) - 131
            width = 230
            height = 40
            region = (int(x), int(y), int(width), int(height))
            # Take screenshot of the region
            screenshot = pyautogui.screenshot(region=region)
            # Save screenshot in current directory
            screenshot_path = "captured_region.png"
            screenshot.save(screenshot_path)
            print(f"Screenshot saved as {screenshot_path}")
            # Extract text using pytesseract
            text = pytesseract.image_to_string(screenshot)
            # Keep only @, =, 0-9, a-z, A-Z, and spaces
            import re
            filtered_text = re.sub(r'[^@=0-9a-zA-Z ]+', '', text)
            print(f"Extracted text: {filtered_text.strip()}")
            pyautogui.click(x+150,y+65)
            pyautogui.write(filtered_text.strip())
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            return point
        else:
            print(f"Image '{image_path}' not found on the screen.")
            return None
    except pyautogui.ImageNotFoundException:
        print(f"Image '{image_path}' not found on the screen (exception caught).")
        return None

def waitLoderToFinish():
    image_path = 'loadingImage.png'  # Replace with your image file path
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if location:
            print(f"Image found at: {location}")
            waitLoderToFinish()
        else:
            print("Image not found on the screen.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen (exception caught).")

def fillDetails():
    pyautogui.write("Digvijay Prasad")
    pyautogui.press("tab")
    pyautogui.write("30")
    pyautogui.press("tab")
    pyautogui.write("M")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("S")
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(.5)

    pyautogui.write("Rekha Kumari")
    pyautogui.press("tab")
    pyautogui.write("26")
    pyautogui.press("tab")
    pyautogui.write("F")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("S")
    pyautogui.press("S")

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    pyautogui.write("7417304083")

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("down")

    pyautogui.press("tab")
    pyautogui.press("tab")

    pyautogui.press("enter")



fillDetails()