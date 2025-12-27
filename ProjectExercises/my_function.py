# General purpose
import os
import numpy as np
import subprocess
from time import sleep
import time
from datetime import datetime
# GPIO related
import RPi.GPIO as GPIO

# camera related
from picamera2 import Picamera2

# General setting
# get the project path
PRJ_PATH = os.getcwd()

# GPIO mode: GPIO.BOARD, GPIO.BCM
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
# Close GPIO warning
GPIO.setwarnings(False)

def image_split_horizontal(img: np.ndarray, pad=20) -> list:
    h, w = img.shape
    columnHist = np.sum(img == 255, axis=0)
    flag = 0
    startList = []
    endList = []
    for col in range(w):
        if flag == 0 and columnHist[col] > 0:
            flag = 1
            startList.append(col)
        elif flag == 1 and columnHist[col] == 0:
            flag = 0
            endList.append(col)
    if flag == 1:
        endList.append(w)
    #padding
    imgList = []
    for i in range(len(startList)):
        start = startList[i]
        end = endList[i]
        digits_area = img[:, start:end]
        digits_area = crop_black_border(digits_area)
        if pad > 0:
            digits_area = add_padding(digits_area, pad)
        imgList.append(digits_area)

    return imgList


def crop_black_border(img):
    rows = np.where(np.sum(img == 255, axis=1) > 0)[0]
    cols = np.where(np.sum(img == 255, axis=0) > 0)[0]
    if len(rows) == 0 or len(cols) == 0:
        return img
    return img[rows[0]:rows[-1]+1, cols[0]:cols[-1]+1]

def add_padding(img: np.ndarray, pad: int, value: int = 0) -> np.ndarray:
    if pad <= 0:
        return img

    h, w = img.shape
    out = np.full((h + 2 * pad, w + 2 * pad), value, dtype=img.dtype)
    out[pad:pad + h, pad:pad + w] = img
    return out




def image_split_vertical(img: np.ndarray, pad=20) -> list:
    h, w = img.shape
    rowHist = np.sum(img == 255, axis=1)
    flag = 0
    startList = []
    endList = []

    for row in range(h):
        if flag == 0 and rowHist[row] > 0:
            flag = 1
            startList.append(row)
        elif flag == 1 and rowHist[row] == 0:
            flag = 0
            endList.append(row)
    if flag == 1:
        endList.append(h)

    imgList = []
    for i in range(len(startList)):
        start = startList[i]
        end = endList[i]
        digits_area = img[start:end, :]
#         digits_area = crop_black_border(digits_area)
#         if pad > 0:
#             digits_area = add_padding(digits_area, pad)
        imgList.append(digits_area)
    return imgList


def led_display(numList: list) -> None:
    # GPIO mode: GPIO.BOARD, GPIO.BCM
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    # Close GPIO warning
    GPIO.setwarnings(False)
    gpio_pins = {
        'a': 21,
        'b': 20,
        'c': 25,
        'd': 8,
        'e': 7,
        'f': 12,
        'g': 1,
        'h': 24
    }

    for pin in gpio_pins.values():
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)


    num_table = {
        0: {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':1,'h':1},
        1: {'a':1,'b':0,'c':0,'d':1,'e':1,'f':1,'g':1,'h':1},
        2: {'a':0,'b':0,'c':1,'d':0,'e':0,'f':1,'g':0,'h':1},
        3: {'a':0,'b':0,'c':0,'d':0,'e':1,'f':1,'g':0,'h':1},
        4: {'a':1,'b':0,'c':0,'d':1,'e':1,'f':0,'g':0,'h':1},
        5: {'a':0,'b':1,'c':0,'d':0,'e':1,'f':0,'g':0,'h':1},
        6: {'a':0,'b':1,'c':0,'d':0,'e':0,'f':0,'g':0,'h':1},
        7: {'a':0,'b':0,'c':0,'d':1,'e':1,'f':1,'g':1,'h':1},
        8: {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':1},
        9: {'a':0,'b':0,'c':0,'d':0,'e':1,'f':0,'g':0,'h':1},
    }

    try:
        for line in numList:
            for num in line:
                for seg, val in num_table[num].items():
                    GPIO.output(gpio_pins[seg], val)
                time.sleep(1)
            for pin in gpio_pins.values():
                GPIO.output(pin, GPIO.HIGH)
            time.sleep(2)
    finally:
        GPIO.cleanup()
        

def take_photo_libcamera() -> str:
    os.environ['DISPLAY'] = ':0'
    preview_proc = subprocess.Popen(
        ["libcamera-hello", "--width", "640", "--height", "480","-t","0"]
    )

    ButtonInputPin = 18   # 按钮输入
    LedInputPin = 4       # LED 输出
    GPIO.setup(ButtonInputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LedInputPin, GPIO.OUT)
    GPIO.output(LedInputPin, GPIO.LOW)

    SaveDirectory = os.path.join(PRJ_PATH, "UserData")
    os.makedirs(SaveDirectory, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.jpg"
    filepath = os.path.join(SaveDirectory, filename)
    GPIO.wait_for_edge(ButtonInputPin, GPIO.BOTH)
    for i in range(3): 
        GPIO.output(LedInputPin, GPIO.HIGH)  # 高电平点亮 LED
        sleep(0.5)
        GPIO.output(LedInputPin, GPIO.LOW)   # 低电平熄灭 LED
        sleep(0.5)
    preview_proc.terminate()
    preview_proc.wait()

    # ===== 使用 Picamera2 拍照 =====
    with Picamera2() as picam2:
        still_config = picam2.create_still_configuration(main={"size": (640, 480)})
        picam2.configure(still_config)
        picam2.start()
        sleep(0.2)
        picam2.capture_file(filepath)
        picam2.stop()

    GPIO.cleanup()
    print(f"拍照完成，保存路径: {filepath}")

    subprocess.run(["xdg-open", filepath])
    return filepath

    