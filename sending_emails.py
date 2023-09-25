import smtplib, ssl

def sending_emails1(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'testing.test.kat@gmail.com'
    password = 'XXXXXXXXXXXXXXXX'

    reciver = 'testing.test.kat@gmail.com'
    
    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username,password)
        server.sendmail(username,reciver,message)

