import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

def message():
    client = Client(account_sid, auth_token)
    transcription = client.transcriptions.list(limit=1)
    sid = transcription[0].sid
    t = client.transcriptions(sid).fetch()
    print(t.transcription_text)
    return str(sid)

if __name__ == '__main__':
    message()