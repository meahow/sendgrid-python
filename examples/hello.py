# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

# sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
sg = sendgrid.SendGridAPIClient(host="http://localhost:5010")
# sg = sendgrid.SendGridAPIClient(host="http://localhost:41010")
from_email = Email("hacktoberfest@gmail.com")
to_email = Email("pszona@gmail.com")
subject = "Hacktoberfest with SendGrid is Fun"
content = Content("text/plain", "3something\nsomething")
mail = Mail(from_email, subject, to_email, content)
print(mail.get())
import pdb; pdb.set_trace()
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)