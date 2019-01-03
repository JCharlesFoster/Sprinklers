from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
# Relay 1
led1 = 26  
led2 = 19 
led3 = 13  
led4 = 6 
led5 = 21 
led6 = 20  
led7 = 16 
led8 = 12 

# Relay 2
led9 = 4 
led10 = 17 
led11 = 27  
led12 = 22 
led13 = 18 
led14 = 23  
led15 = 24 
led16 = 25 

# Set each pin as an output and make it low:
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)
GPIO.setup(led8, GPIO.OUT)
 # Relay 2
GPIO.setup(led9, GPIO.OUT)
GPIO.setup(led10, GPIO.OUT)
GPIO.setup(led11, GPIO.OUT)
GPIO.setup(led12, GPIO.OUT)
GPIO.setup(led13, GPIO.OUT)
GPIO.setup(led14, GPIO.OUT)
GPIO.setup(led15, GPIO.OUT)
GPIO.setup(led16, GPIO.OUT)

@app.route("/")
def main():
   return render_template('main.html')


@app.route("/<pin>/<action>")
def action(pin, action):
   if pin == "pin1" and action == "on":
      GPIO.output(led1, GPIO.HIGH)
   
   if pin == "pin1" and action == "off":
      GPIO.output(led1, GPIO.LOW)
   
   if pin == "pin2" and action == "on":
      GPIO.output(led2, GPIO.HIGH)
   
   if pin == "pin2" and action == "off":
      GPIO.output(led2, GPIO.LOW)
      
   if pin == "pin3" and action == "on":
      GPIO.output(led3, GPIO.HIGH)
   
   if pin == "pin3" and action == "off":
      GPIO.output(led3, GPIO.LOW) 
      
   if pin == "pin4" and action == "on":
      GPIO.output(led4, GPIO.HIGH)
   
   if pin == "pin4" and action == "off":
      GPIO.output(led4, GPIO.LOW) 
      
   if pin == "pin5" and action == "on":
      GPIO.output(led5, GPIO.HIGH)
   
   if pin == "pin5" and action == "off":
      GPIO.output(led5, GPIO.LOW) 
      
   if pin == "pin6" and action == "on":
      GPIO.output(led6, GPIO.HIGH)
   
   if pin == "pin6" and action == "off":
      GPIO.output(led6, GPIO.LOW) 
      
   if pin == "pin7" and action == "on":
      GPIO.output(led7, GPIO.HIGH)
   
   if pin == "pin7" and action == "off":
      GPIO.output(led7, GPIO.LOW) 
      
   if pin == "pin8" and action == "on":
      GPIO.output(led8, GPIO.HIGH)
   
   if pin == "pin8" and action == "off":
      GPIO.output(led8, GPIO.LOW) 
      
   # Relay board 2 
      
   if pin == "pin9" and action == "on":
      GPIO.output(led9, GPIO.HIGH)
   
   if pin == "pin9" and action == "off":
      GPIO.output(led9, GPIO.LOW)
   
   if pin == "pin10" and action == "on":
      GPIO.output(led10, GPIO.HIGH)
   
   if pin == "pin10" and action == "off":
      GPIO.output(led10, GPIO.LOW)
      
   if pin == "pin11" and action == "on":
      GPIO.output(led11, GPIO.HIGH)
   
   if pin == "pin11" and action == "off":
      GPIO.output(led11, GPIO.LOW) 
      
   if pin == "pin12" and action == "on":
      GPIO.output(led12, GPIO.HIGH)
   
   if pin == "pin12" and action == "off":
      GPIO.output(led12, GPIO.LOW) 
      
   if pin == "pin13" and action == "on":
      GPIO.output(led13, GPIO.HIGH)
   
   if pin == "pin13" and action == "off":
      GPIO.output(led13, GPIO.LOW) 
      
   if pin == "pin14" and action == "on":
      GPIO.output(led14, GPIO.HIGH)
   
   if pin == "pin14" and action == "off":
      GPIO.output(led14, GPIO.LOW) 
      
   if pin == "pin15" and action == "on":
      GPIO.output(led15, GPIO.HIGH)
   
   if pin == "pin15" and action == "off":
      GPIO.output(led15, GPIO.LOW) 
      
   if pin == "pin16" and action == "on":
      GPIO.output(led16, GPIO.HIGH)
   
   if pin == "pin16" and action == "off":
      GPIO.output(led16, GPIO.LOW) 

   return render_template('main.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
