import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os #enter your gmail app passcode
to="narutothop@gmail.com"
#enter whom you want to send
From="nsingamsetti11@gmail.com"
subject = "Mail with attachment"
text = "Sample test mail for attachment sending" #body
#body of mail
attach= 'list1.py' #give your attachment name
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text))
#to load and encode the attachment
part=MIMEBase("application","octet-stream")
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
                'attachment;filename="%s"' % os.path.basename(attach))
msg.attach(part)
#server connection starts..
mailserver=smtplib.SMTP("smtp.gmail.com",587)
mailserver.starttls()
mailserver.login(From,"dqfo gdpo vkbd rnuf")
mailserver.sendmail(From,to,msg.as_string())
print("Done")
#close the connection
mailserver.close()


