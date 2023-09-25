import requests
import smtplib, ssl
from sending_emails import sending_emails1

api_key = 'a21ddf713e52419abfc63f3cce140ffc'

url1 = 'https://news.google.com/home'
topic = 'tesla'

url = f'https://newsapi.org/v2/everything?q={topic}&from=2023-08-25&sortBy=publishedAt&'\
'apiKey=a21ddf713e52419abfc63f3cce140ffc&language=en'

#getting url with requests
request = requests.get(url)
content = request.json()


new_title = ''
for article in content['articles'][:20]:
    #getting data content from api
    new_title = new_title +  article['title'] +'\n' + article['description']+ '\n'+ article['url'] + 2*'\n'
# adding subject
message_new = "Subject: today news"+ '\n' + new_title
#converting to encode ... taking care of error 
message_new= message_new.encode('utf-8')

#sending email 
sending_emails1(message=message_new)

#host = 'smtp.gmail.com'
#port = 465

#user_name = 'testing.test.kat@gmail.com'
#user_pass = 'XXXXXXXXXXXXXX'
#reciver_email = 'katcode.py@gmail.com'

#with smtplib.SMTP_SSL(host, port) as server:
#    server.login(user_name,user_pass)
#    server.sendmail(user_name,reciver_email,message_new)

