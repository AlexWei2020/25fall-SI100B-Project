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
GPIO.setmode(GPIO.BOARD)
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





def led_display(numList:list)->None:
    """
    Function description: Build a digital tube display circuit on the breadboard. Display the result with the digital tube.
    Tips:
    1.The GPIO mode we used is GPIO.BOARD. 
    2.The digital tube is common anode. Use GPIO port to input high level for digital tube power pin.
    3. After the LED lamp pin of the digital tube is connected to the GPIO pin, the corresponding relationship can be confirmed by lighting the led one by one.
    4. Check "function introduction.xlsx" for GPIO functions.
    
    :para numList: input numbers in list to be displayed.
    :return: None
    """

    ### write your codes here ###
    #############################
    # step 1:
    # Clarify the relationship between led pins and GPIO pins
    # Set the GPIO pins to GPIO.OUT mode and give them the right output
      
    
    
    
    
    # step 2:
    # Clarify the led composition of each number
    
    
    
      
        
    # step 3:
    # Display the numbers in the list one by one
    # Display every number for 1 second
    # Wait two seconds when displaying different lines
    
    
    
    
    
    
    ret = None
    return ret


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