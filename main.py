# main.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pathlib import Path
import slack
from tools import send_slack_message

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize your Flask app
app = Flask(__name__)

global slack_client
slack_client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

@app.route('/messages', methods=['POST'])
def handle_send():
    data = request.json
    channel = data['channel']
    message_body = data['message_body']
    message_type = data.get('message_type', 'message')
    code_snippet = data.get('code_snippet', None)

    send_slack_message(slack_client, channel, message_body, message_type, code_snippet)

    return jsonify({"status": "success", "message": "Message processing initiated."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)