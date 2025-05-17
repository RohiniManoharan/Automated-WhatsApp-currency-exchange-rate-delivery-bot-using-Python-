# import required packages
import requests
import time
from twilio.rest import Client


API_KEY = "1************************" # enter your Api_key from the exchangerate-api.com
COUNTRY=" INR"
TWILIO_SID = "A*********************" # enter your twilio SID
TWILIO_AUTH_TOKEN = "E**************" # enter your twilio Token"
FROM_WHATSAPP_NUMBER = "whatsapp:+14155238886"
TO_WHATSAPP_NUMBER = "whatsapp:+1************" # enter your telephone number

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def get_latest_news():
   url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"{API_KEY}/"
        f"latest/CAD"
           )
    response = requests.get(url)
    data = response.json()
    print("status code",response.status_code)
    print("response:",response.text)
    if data["result"] == "success" :
        messages=[]
        msg = "Today's INR rate for CAD:"
        message=messages,data["conversion_rates"]["INR"]
        message = f"🗞️ *{msg}*{message} "
        messages.append(message)
        return message
    return "⚠️ No update found."

def send_whatsapp_message(message):
    client.messages.create(
        from_=FROM_WHATSAPP_NUMBER,
        body=message,
        to=TO_WHATSAPP_NUMBER
    )

while True:
    print("waiting for latest update")
    currencyrate = get_latest_news()
    print("sending to whatsapp")
    send_whatsapp_message(currencyrate)
    time.sleep(3600)  # Every hour
