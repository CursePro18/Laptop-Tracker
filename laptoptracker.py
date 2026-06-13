import cv2
import requests
import time
import pyautogui
import pygame
import os

# =========================
# WAIT AFTER BOOT
# =========================

time.sleep(10)

# =========================
# TELEGRAM CONFIG
# =========================

TOKEN = "8894294193:AAE2l7F9pWo6e5g5sffifU_MGfgzvRC7K7E"
CHAT_ID = "6860723254"
# =========================
# CAMERA PHOTO
# =========================

try:

    cam = cv2.VideoCapture(0)

    time.sleep(3)

    ret, frame = cam.read()

    if ret:

        image_name = "thief_hd.jpg"

        cv2.imwrite(
            image_name,
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 100]
        )

        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

        with open(image_name, "rb") as photo:

            requests.post(
                url,
                data={"chat_id": CHAT_ID},
                files={"photo": photo}
            )

        print("Photo Sent")

    else:

        print("Camera Failed")

    cam.release()

except Exception as e:

    print("Camera Error:", e)

# =========================
# SCREENSHOT
# =========================

try:

    screenshot = pyautogui.screenshot()

    screen_name = "screenshot.png"

    screenshot.save(screen_name)

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(screen_name, "rb") as photo:

        requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": photo}
        )

    print("Screenshot Sent")

except Exception as e:

    print("Screenshot Error:", e)

# =========================
# LOCATION
# =========================

try:

    data = requests.get(
        "https://ipinfo.io/json"
    ).json()

    city = data.get("city")
    region = data.get("region")
    country = data.get("country")
    loc = data.get("loc")
    ip = data.get("ip")

    latitude, longitude = loc.split(",")

    google_maps = (
        f"https://www.google.com/maps?q="
        f"{latitude},{longitude}"
    )

    message = f"""
🚨 LAPTOP STARTED 🚨

🌐 IP:
{ip}

📍 Location:
{city}, {region}, {country}

📌 Coordinates:
{latitude}, {longitude}

🗺 Google Maps:
{google_maps}
"""

    url = (
        f"https://api.telegram.org/"
        f"bot{TOKEN}/sendMessage"
    )

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Location Sent")

except Exception as e:

    print("Location Error:", e)

# =========================
# ALARM
# =========================

try:

    pygame.init()

    pygame.mixer.init()

    pygame.mixer.music.load(
        r"C:\Users\adity\OneDrive\Desktop\Hacker Tracker\alarm.mpeg"
    )

    pygame.mixer.music.play()

    time.sleep(15)

except Exception as e:

    print("Alarm Error:", e)

# =========================
# CLEANUP FILES
# =========================

try:

    if os.path.exists("thief_hd.jpg"):
        os.remove("thief_hd.jpg")

    if os.path.exists("screenshot.png"):
        os.remove("screenshot.png")

except:
    pass