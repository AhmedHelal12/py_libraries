import smtplib

sender = 'ahmedhelalragab@gmail.com'
recipient = 'ahmedhelalragab@gmail.com'
password = str(input("Enter the password: "))
message = "Subject: It's me. \n Hi Ahmed from Ahmed"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,recipient,message)
server.quit()


