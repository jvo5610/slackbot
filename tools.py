import slack

def send_slack_message(slack_client, channel, message_body, message_type="message", code_snippet=None):

    # Initialize the blocks array
    blocks = []
    
    # Add the initial message or alert block with bold formatting
    if message_type == "alarm":
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*🚨 New Alarm Triggered!:*"
            }
        })
    elif message_type == "message":
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*✉️ Message:*"
            }
        })
    else:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*❓ Unknown Message Type:*"
            }
        })
    
    # Add the main message body as a separate block
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": message_body
        }
    })
    
    # Add the code snippet block if provided
    if code_snippet:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"```{code_snippet}```"
            }
        })
    
    try:
        response = slack_client.chat_postMessage(
            channel=channel,
            blocks=blocks
        )
        print("Message sent successfully:", response.data)
    except slack.errors.SlackApiError as e:
        print(f"Failed to send message with error: {e.response['error']}")
