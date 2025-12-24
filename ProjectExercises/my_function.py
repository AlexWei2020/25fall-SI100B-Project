# General purpose
import os
import numpy as np
from time import sleep
import time

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
        start = max(0, startList[i] - pad)
        end = min(w, endList[i] + pad)
        digits_area = img[:, start:end]
        imgList.append(digits_area)

    return imgList





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
    #padding
    imgList = []
    for i in range(len(startList)):
        start = max(0, startList[i] - pad)
        end = min(h, endList[i] + pad)
        digits_area = img[start:end, :]
        imgList.append(digits_area)

    return imgList

def led_display(numList: list) -> None:
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
            time.sleep(2)
    finally:
        GPIO.cleanup()
        
        
def take_photo_libcamera()->str:
    """
    Function description: Build the camera control circuit on the breadboard. After pressing the control button, the shooting indicator(led light) lights up and the camera takes a picture.
    Tips:
    1. Use the 3.3v and GND pins on the Raspberry Pi as the power and ground of the circuit.
    2. Use the GPIO port as a signal line to sense the occurrence of key events. Set the correct GPIO mode
    3. Create a camera obj and wait for a button press to take a photo.
    4. Save the picture to /UserData/.
    5. Clean the camera.
    
    :para
    :return: a string which contains the picture location
    """

    ### write your codes here ###
    #############################
    # step 1: 
    #set a GPIO as an input channel for detecting
     
    
    
    
    
    
    # step 2: 
    # create the camera obj and wait for a button to take a photo
    # recorder the saving path
    # clear the camera
    
    
    
    
    
    
    # step3:
    # return the saving path 
    
    
    
    
    
    
    ret = None
    return ret