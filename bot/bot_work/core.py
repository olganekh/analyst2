from telegram.ext import Updater, CommandHandler
from analyst_bot.settings import TOKEN_TELEGRAM_BOT_API
from bot.bot_work.start_command import start, help, cancel, ready_to_chat


def run_bot():
    """Основа бота: прокинули токен, подкючили команду старт, создали пулинг"""

    updater = Updater(TOKEN_TELEGRAM_BOT_API)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('cancel', cancel))
    dp.add_handler(CommandHandler('ready_to_chat', ready_to_chat))

    # dp.add_handler(CommandHandler('error', error))

    updater.start_polling()
    updater.idle()