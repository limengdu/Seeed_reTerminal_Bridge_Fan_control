import sys 
import time
try:
	import RPi.GPIO as GPIO	
except RuntimeError:
	print("Error importting Rpi.GPIO")

MAX_TEMP = 40.0
MIN_TEMP = 20.0
 
def cpu_temp():
	f = open("/sys/class/thermal/thermal_zone0/temp",'r') 
	return float(f.read())/1000
 
def main():
	channel = 23
	GPIO.setmode(GPIO.BCM)
	
	# init 23 off
	GPIO.setup(channel,GPIO.OUT,initial=GPIO.LOW)
	is_close = True
	while 1:
		temp = cpu_temp()
		if is_close:
			if temp > MAX_TEMP:
				GPIO.output(channel,GPIO.HIGH)
				is_close = False
		else:
			if temp < MIN_TEMP:
				GPIO.output(channel,GPIO.LOW)
				is_close = True
		time.sleep(2.0)
		GPIO.setwarnings(False) 
 
if __name__ == '__main__':
	main()	
