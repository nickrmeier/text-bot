from twilio.rest import Client

account_sid = 'account sid'
auth_token = 'auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='twilio number',
    body='have an excellent day',
    to='approved number'
)

print(message.sid)
