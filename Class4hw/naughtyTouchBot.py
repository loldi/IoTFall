
import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "touchedmynonoarea@gmail.com"
toaddr = "genu4ldi@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "I'VE BEEN TOUCHED!"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.IN)
GPIO.setup(12,GPIO.IN)
prev_input = 0
prev_input2 = 0

while True:
  input = GPIO.input(7)
  if ((not prev_input) and input):
    body = "I've been touched in my upstairs no-no area!"

  prev_input = input
  msg.attach(MIMEText(body, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(fromaddr, "fuckoffsafari")
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

  input2 = GPIO.input(12)
  if (( prev_input2) and not input2):
    body = "I've been touched in my downstairs no-no area!"
 #    msg.attach(MIMEText(body, 'plain'))
 
	# server = smtplib.SMTP('smtp.gmail.com', 587)
	# server.starttls()
	# server.login(fromaddr, "fuckoffsafari")
	# text = msg.as_string()
	# server.sendmail(fromaddr, toaddr, text)
	# server.quit()
  prev_input2 = input2
  
  time.sleep(0.05)
GPIO.cleanup()


