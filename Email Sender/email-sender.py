import smtplib

sender = 'quaid.johar33@gmail.com'
receivers = ['recipient@email.com']
msg = "This is a test email message"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('quaid.johar33@gmail.com', 'xxx-password-xxx')

server.sendmail(sender, receivers, msg)
print('Mail sent successfully')
