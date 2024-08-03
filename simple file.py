#sending a simple mail using python
#smptlib--->simple mail transfer protocol
#Email OTP Authentication
import random
import math
import smtplib

#we will generate a 6 digit otp by using base digits
digits="0123456789"
OTP=""  #empty string

#now we will use math module along with module to generate 6 digit otp
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    #print(OTP)
otp=OTP+"is your OTP"
mssg=otp
#include our email automation
s=smtplib.SMTP("smtp.gmail.com",587)#587 is port
#or we can directly use smtplib.SMTP_SSL("smtp.gmail.com",465)
#similar to tls SSL secures the data and transfers it
s.starttls()
s.login("nsingamsetti11@gmail.com","dqfo gdpo vkbd rnuf")
user="nsingamsetti11@gmail.com"
email=input("enter the mail which you want to send:")
s.sendmail(user,email,mssg)
while True:
    a=input("enter your OTP: ")
    if a==OTP:
        print("OTP CRRCT")
    else:
        print("Failure wrong OTP")
