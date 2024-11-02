data = {
    "content": "Hello, this is a test message!"
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Webhook sent successfully.")
else:
    print(f"Failed to send webhook. Status code: {response.status_code}")
    print(f"Response: {response.text}")
