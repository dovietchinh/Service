import requests

# Your bot's token
TOKEN = "MY_TOKEN"
# The chat ID of the recipient (group chat or individual)
CHAT_ID = "CHAT_ID"
# The text message you want to send
MESSAGE_TEXT = "Hello, this is a message from my Telegram bot!"

def send_telegram_message(chat_id, text):
    # Telegram API endpoint
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # Parameters to be sent with the POST request
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    # Make a POST request to the Telegram API
    response = requests.post(url, data=payload,timeout=10)
    return response.json()  # Return the JSON response from the API

# Send the message
response = send_telegram_message(CHAT_ID, MESSAGE_TEXT)
print(response)  # Print the API response to check if the message was sent successfully