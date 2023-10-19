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
    except Exception as e:
        print(f"An error has occurred {e}")


async def send_msg(bot_token, chat_id, msg_body, attachement_urls=[]):
    """Send message to given Telegram chat"""
    bot = telegram.Bot(bot_token)

    attachement_count = len(attachement_urls)

    async with bot:
        if attachement_count != 0:
            url = attachement_urls[0]
            await bot.send_document(chat_id=chat_id, document=url, caption=msg_body, parse_mode='MarkdownV2')
            
            for i in range(1, attachement_count):
                url = attachement_urls[i]
                await bot.send_document(chat_id=chat_id, document=url)
        else:
            await bot.send_message(chat_id=chat_id, text=msg_body, disable_web_page_preview=True, parse_mode='MarkdownV2')
            

if __name__ == "__main__":
    main()


