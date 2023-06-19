
# this code is to check that twilio has been connected to your phn
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "write your account sid of twilio"
# Your Auth Token from twilio.com/console
auth_token  = "your twilio token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:[your registered number]'
)
print(message.sid)
