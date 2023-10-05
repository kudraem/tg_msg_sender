import argparse
import asyncio
from telegram import Bot

def main():
    parser = argparse.ArgumentParser(
                        prog='TgUtility',
                        description='Telegram useful utilities',
                        epilog='Enjoy it')

    parser.add_argument('bot_token',
                        help='Telegram bot api token')
    parser.add_argument('command',
                        choices=['get-last-active-chat'],
                        help='Command to execute')

    args = parser.parse_args()

    try:
        chat_id = asyncio.run(get_last_active_chat_id(args.bot_token))
        if (chat_id is None):
            print('No recent messages found')
        else:
            print(f"Last active chat ID is '{chat_id}'")
    except Exception as e:
        print(f"An error has occurred: {e}")
    

async def get_last_active_chat_id(bot_token):
        bot = Bot(bot_token)
        async with bot:
            updates = await bot.get_updates()
        
        chat_id = None

        if updates:
            chat_id = updates[-1].message.chat_id
        
        return chat_id


if __name__ == '__main__':
    main()
