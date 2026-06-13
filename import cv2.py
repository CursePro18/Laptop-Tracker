import cv2
import requests
import time

TOKEN = "8894294193:AAE2l7F9pWo6e5g5sffifU_MGfgzvRC7K7E"
CHAT_ID = "6860723254"

# Open Camera
cam = cv2.VideoCapture(0)

# Set HD Resolution
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Camera ko warmup time
time.sleep(2)

ret, frame = cam.read()

if ret:

    image_name = "thief_hd.jpg"

    # Better quality save
    cv2.imwrite(image_name, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

    # Send Photo
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(image_name, "rb") as photo:

        requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": photo}
        )

    print("HD Photo Sent")

else:
    print("Camera Error")

cam.release()