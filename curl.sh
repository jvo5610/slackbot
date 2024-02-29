curl -X POST http://localhost:3000/messages \
     -H "Content-Type: application/json" \
     -d '{"channel": "varios", "message_body": "Here is the main content of the message."}'
