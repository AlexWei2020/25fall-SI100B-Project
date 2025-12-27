import RPi.GPIO as GPIO
import time

# GPIO 模式
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO 与数码管段的对应关系（按你的接线）
# 21-a，20-b，12-f，1-g，7-e，8-d，25-c，24-h
segments = [
    ('a', 21),
    ('b', 20),
    ('f', 12),
    ('g', 1),
    ('e', 7),
    ('d', 8),
    ('c', 25),
    ('h', 24),
]

pins = [pin for _, pin in segments]

# 共阳极：默认全灭（高电平）
GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        for name, pin in segments:
            print(f"Should light segment: {name} (GPIO {pin})")

            # 全灭
            GPIO.output(pins, GPIO.HIGH)
            # 只点亮当前段（共阳极：低电平亮）
            GPIO.output(pin, GPIO.LOW)

            time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
