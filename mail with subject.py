#now we will add subject and make sure to adress
#is visible along with the body
#of email using email package
import smtplib
#mime--->multi purpose internet mail extension protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#defining data
From="nsingamsetti11@gmail.com"
to="narutothop.@gmail.com"
subject="Python Course"
msg= MIMEMultipart()
msg["From"]=From
msg["To"]=to
msg["Subject"]=subject
body="Hello! first mail using python script"
#the \n seperates the mssg
msg.attach(MIMEText(body,"plain"))
text=msg.as_string()
#same usage of smtplib to start the process
server = smtplib.SMTP("smtp.gmail.com",587)
#or we can directly use smtplib.SMTP_SSL("smtp.gmail.com",465)
#similar to tls SSL secures the data and transfers it
server.starttls()
#next, log into server
server.login(From,"dqfo gdpo vkbd rnuf")
#give your app passcode here
#send the mail
server.sendmail(From,to,text)
print("mail sent")
server.quit()


