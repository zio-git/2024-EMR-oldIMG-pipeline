import requests

# The URL and endpoint of the SMS gateway API
url = 'https://echo.hismalawi.org/api/v1/sms/outbounds/'

# The phone number you want to send the SMS to
to_phone_number = '+265995246144'

# The phone number or sender ID associated with your SMS gateway account
from_phone_number = '+2652479'

# The message you want to send
message = 'Hello from SMS gateway!'

# Your authorization token or API key
api_token = 'fe722faaa8f09438c79e70b2564729d9d1026027'

# Set the content-type and authorization headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

# Create a dictionary with the message details
payload = {
    'to': to_phone_number,
    'from': from_phone_number,
    'message': message
}

try:
    # Send the HTTP POST request to the SMS gateway API
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print('SMS sent successfully.')
    else:
        print(f'Error occurred while sending SMS. Status code: {response.status_code}')
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f'Error occurred while sending SMS: {str(e)}')

