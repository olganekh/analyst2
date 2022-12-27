from logging import Logger
import datetime


from telegram import ReplyKeyboardMarkup
from db_analyst.models import User_verification
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger: Logger = logging.getLogger(__name__)


def start(update, context, button=None):
    chat = update.effective_chat
    name = update.message.chat.first_name
    User_verification.objects.get_or_create(user_id=chat.id, activating_bot=True, name=name)
    button = ReplyKeyboardMarkup([['/ready_to_chat'], ['/cancel'], ['/help']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Я бот, который позволит тебе проанализировать бюджет при постановки цели.\n'
             'Рассказать тебе, что умею: \n'
             'При нажатии команды "/ready_to_chat", готов к общению.\n'
             'При нажатии команды "/cancel", распрощаемся.\n'
             'Если возникнут вопросы, то ты всегда можешь нажать "/help".\n'.format(name),
        reply_markup=button
    )


def help(update, context, button=None):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/ready_to_chat'], ['/cancel']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Давай расскажу тебе подробнее чем я занимаюсь: \n'
             'Команда ready_to_chat необходима для того, чтобы запустить процесс расчета твоих финансовых трат. \n'
             'Врезультате получите отчет как правельно распорядится своим доходом \n'
             'Eсли интересно нажатии команды "/ready_to_chat", готов к общению.\n'
             'Если нет, нажатии команды "/cancel", распрощаемся.\n'.format(name),
        reply_markup=button
    )


def cancel(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Досвидания! {}'.format(name),

    )


def ready_to_chat(update, context):

    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Начнем! {}.Давай выбирим цели:'.format(name)
    )