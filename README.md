# Telegram Message Sender
Package to send telegram messages with attachements.

# Usage
## import module
```
from tg_msg_sender.sender import send_msg

# text message
bot_token = 'BOT_TOKEN'
chat_id = 'CHAT_ID'
msg_text = 'Hello, my friend 🐍'
send_msg(bot_token, chat_id, msg_text)

## text message with attachements
attachements = ['https://foo.com/bar.jpeg', 'https://bar.com/foo.mov']
send_msg(bot_token, chat_id, msg_text, attachements)
```

## cli command
```
send-tg-msg CHAT_ID 'Hello, my friend 🐍' BOT_TOKEN
```

# Utilities
To check last active telegram chat id, you can use 'tg-utility' command:
`tg-utility BOT_TOKEN`
