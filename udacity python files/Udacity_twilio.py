# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 01:06:42 2016

@author: p2admin
"""

from twilio.rest import TwilioRestClient

account_sid = "AC05c1e51cc11fe364f481f293628ef130" # Your Account SID from www.twilio.com/console
auth_token  = "56b29a79d7b7ee053bd6fbd96e2ae2e9"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body=" You are awesome!!!!!!!!!!!!!,",                             
    to="+14807580332",    # Replace with your phone number
    from_="+1(616) 710-4598	") # Replace with your Twilio number

print(message.sid)
