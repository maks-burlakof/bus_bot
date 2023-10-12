from telebot.types import Message, CallbackQuery

from botclass import MyBot
from actions import Generic, Notify, Track, Parse


def initialize(bot: MyBot):

    # Basic commands
    generic = Generic(bot)

    @bot.message_handler(commands=['start'], func=generic.is_allowed_user)
    def start(message: Message):
        generic.start(message)

    @bot.message_handler(commands=['register'])
    def register(message: Message):
        generic.register(message)

    @bot.message_handler(commands=['settings'], func=generic.is_allowed_user)
    def settings(message: Message):
        generic.settings(message)

    @bot.message_handler(commands=['extra'])
    def extra(message: Message):
        generic.extra(message)

    @bot.message_handler(commands=['description'])
    def description(message: Message):
        generic.description(message)

    @bot.message_handler(commands=['faq'], func=generic.is_allowed_user)
    def faq(message: Message):
        generic.faq(message)

    @bot.message_handler(commands=['feedback'])
    def feedback(message: Message):
        generic.feedback(message)

    @bot.message_handler(commands=['announcement'], func=generic.is_admin)
    def announcement_text(message: Message):
        generic.announcement_text(message)

    @bot.message_handler(commands=['announcement_auto'], func=generic.is_admin)
    def announcement_auto(message: Message):
        bot.send_message_quiet(message.chat.id, bot.m('not_implemented'))

    @bot.message_handler(commands=['users'], func=generic.is_admin)
    def users_list(message: Message):
        generic.users_list(message)

    @bot.message_handler(commands=['ban'], func=generic.is_admin)
    def ban_user(message: Message):
        generic.ban_user(message)

    @bot.message_handler(commands=['database'], func=generic.is_admin)
    def database_view(message: Message):
        generic.database_view(message)

    @bot.message_handler(commands=['invite_codes'], func=generic.is_admin)
    def invite_codes_view(message: Message):
        generic.invite_codes_view(message)

    @bot.message_handler(commands=['invite_codes_create'], func=generic.is_admin)
    def invite_codes_create(message: Message):
        generic.invite_codes_create(message)

    @bot.message_handler(commands=['logs'], func=generic.is_admin)
    def logs_send(message: Message):
        generic.logs_send(message)

    @bot.message_handler(commands=['clear_logs'], func=generic.is_admin)
    def logs_clear(message: Message):
        generic.logs_clear(message)

    @bot.message_handler(commands=['exit'], func=generic.is_admin)
    def exit_bot(message: Message):
        generic.exit_bot(message)

    @bot.message_handler(commands=['secret'])
    def secret(message: Message):
        generic.secret(message)

    # Notify
    notify = Notify(bot)

    @bot.message_handler(commands=['notify'], func=generic.is_allowed_user)
    def notify_start(message: Message):
        notify.start(message)

    @bot.callback_query_handler(func=lambda call: call.data.startswith(notify.markups.prefix))
    def notify_callback(call: CallbackQuery):
        notify.callback(call)

    # Track
    track = Track(bot)

    @bot.message_handler(commands=['track'], func=generic.is_allowed_user)
    def track_start(message: Message):
        track.start(message)

    @bot.callback_query_handler(func=lambda call: call.data.startswith(track.markups.prefix))
    def track_callback(call: CallbackQuery):
        track.callback(call)

    # Unknown command
    @bot.message_handler()
    def ordinary_text(message: Message):
        generic.ordinary_text(message)



















