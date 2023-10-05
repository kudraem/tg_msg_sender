import argparse
import asyncio
import telegram

def main():
    parser = argparse.ArgumentParser(
                        prog="TgMessageSend",
                        description="""Send message with attachements 
                                     to Telegram chat""",
                        epilog="Enjoy it")

    parser.add_argument("chat_id", 
                        help="Telegram chat ID to send message")
    parser.add_argument("message_body", 
                        help="Message text body")
    parser.add_argument("bot_token", 
                        help="Telegram bot api token")
    parser.add_argument("-a", "--attachements",
                        default=[],
                        nargs="+",
                        help="URL list of attachements to message")

    args = parser.parse_args()

    try:
        asyncio.run(send_msg(args.bot_token, args.chat_id, args.message_body, args.attachements))
    except:
        print("An error has occurred")


async def send_msg(bot_token, chat_id, msg_body, attachement_urls=[]):
    """Send message to given Telegram chat"""
    bot = telegram.Bot(bot_token)
    async with bot:
        for url in attachement_urls:
            await bot.send_document(chat_id=chat_id, document=url)
        await bot.send_message(chat_id=chat_id, text=msg_body, disable_web_page_preview=True)


if __name__ == "__main__":
    main()


