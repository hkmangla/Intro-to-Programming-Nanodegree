from twilio import rest
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC6a965ae368716c44f7a5715c369307fd"
auth_token  = "e85edb394b4b406f1f1510fd50ff8f16"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Kesa lga bhai, It's a symbol of success. Is not it?",
    to="+919671102079",    # Replace with your phone number
    from_="+12017201944") # Replace with your Twilio number
print message.sid