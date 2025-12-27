from my_function import take_photo_libcamera

if __name__ == "__main__":
    photo_path = take_photo_libcamera()
    print("Photo saved at:", photo_path)
    
# import RPi.GPIO as GPIO
# from time import sleep
# 
# LedPin = 4
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LedPin, GPIO.OUT)

# print("LED 测试：闪烁 5 次")
# for _ in range(5):
#     GPIO.output(LedPin, GPIO.HIGH)  # 高电平点亮 LED
#     sleep(0.5)
#     GPIO.output(LedPin, GPIO.LOW)   # 低电平熄灭 LED
#     sleep(0.5)

# GPIO.cleanup()
# print("LED 测试完成")
