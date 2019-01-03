import RPi.GPIO as GPIO
import time

zones = []

def setup_zones():
	GPIO.setmode(GPIO.BCM)
	zone_one = Zone(26, True, 1)
	zones.append(zone_one)


def toggle_gpio(zone):
	if zone.activated:
		GPIO.output(zone.pin, GPIO.LOW)
		zone.activated = False
	else:
		GPIO.output(zone.pin, GPIO.HIGH)
		zone.activated = True


def main():
	setup_zones()
	while(True):
		time.sleep(10)
		toggle_gpio(zones[0])


class Zone(object):
	
	activated = False
	pin = None
	zone_number = None
	
	def __init__(self, pin, activated, zone_number):
		self.pin = pin
		self.activated = activated
		self.zone_number = zone_number
		
		self.setup_zone()
		
	def setup_zone(self):
		GPIO.setup(self.pin, GPIO.OUT)
		
if __name__ == "__main__":
   main()
