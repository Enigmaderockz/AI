import requests

# Define the Teams webhook URL
webhook_url = 'https://<your_teams_tenant>.webhook.office.com/webhookb2/<your_webhook_id>/IncomingWebhook/<your_incoming_webhook_id>'

# Define the message payload
message = {
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "themeColor": "0072C6",
    "title": "New task assigned",
    "text": "A new task has been assigned to you.",
    "potentialAction": [
        {
            "@type": "OpenUri",
            "name": "View task",
            "targets": [
                {
                    "os": "default",
                    "uri": "https://example.com/tasks/1234"
                }
            ]
        }
    ]
}

# Send the message to Teams
response = requests.post(webhook_url, json=message)

# Check the response status code
if response.status_code == 200:
    print('Message sent successfully.')
else:
    print('Failed to send message: ' + response.text)

    
  This code uses the requests library to send an HTTP POST request to the Microsoft Teams webhook URL, passing a JSON payload containing the message details. The potentialAction property in the payload specifies an action that can be taken when the user clicks a button in the message card. In this case, the action is to open a URI that points to a specific task in your application.

Note that you will need to replace the placeholders in the webhook_url variable with the actual values for your Teams webhook. You can create a webhook URL in Microsoft Teams by going to the channel where you want to post messages, clicking on the three dots icon, and selecting "Connectors". From there, you can choose the "Incoming Webhook" connector and follow the prompts to create a new webhook.
