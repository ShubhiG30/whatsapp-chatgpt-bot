from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc310fadde63a758578b47082b59e759c"
# Your Auth Token from twilio.com/console
auth_token  = "3af5ddf1f322b6b1a0722c772d09a273"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+919653094417'
)
print(message.sid)