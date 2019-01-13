import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pin = 12
GPIO.setup(pin, GPIO.IN)
data = []
condition = False
while True:
        if GPIO.input(pin) == GPIO.HIGH:
            data.append(GPIO.HIGH)
            condition = True
        elif condition:
              with open('data.txt', 'w') as f:
                      f.write('\n'.join(str(data)))
                      f.close()
              data=[]
              print('Done')
              condition = False
