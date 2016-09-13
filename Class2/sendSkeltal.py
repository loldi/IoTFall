import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
fromaddr = "*******"
toaddr = raw_input("WHO DO YOU WANT TO SPOOK?: ")
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "VERY IMPORTANT EMAIL CHECK PLS"

whoBy = raw_input("WHO IS SENDING THIS SPOOPY EMAIL??: ")

replyPrompt = raw_input("WHAT MESSAGE DO YOU WANT BACK???: ")

timeResponse = raw_input("HOW MUCH TIME DO THEY HAVE???: ")

orElse = raw_input("WHAT ARE THE CONSEQUENCES???: ")
 
body = "YOU HAVE BEEN EMAILED BY {}, REPLY WITH {} IN {} SECONDS OR {}".format(whoBy, replyPrompt, timeResponse, orElse)
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "hunter2")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()




