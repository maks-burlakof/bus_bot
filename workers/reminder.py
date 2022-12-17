from logging import getLogger, config
from datetime import date, timedelta
from os import environ

from message_texts import *
from clients import *
from actioners import UserActioner

config.fileConfig(fname='logging_config.conf', disable_existing_loggers=False)
logger = getLogger(__name__)

TOKEN = environ.get("TOKEN")

# days before the bus
TIME_DELTA = 29


class Reminder:
    GET_NOTIFY_DATE = f'SELECT chat_id, user_id FROM users WHERE (julianday(notify_date) - julianday() < {TIME_DELTA});'

    GET_TRACK_DATA = 'SELECT chat_id, user_id, track_data FROM users WHERE track_data NOT NULL;'

    def __init__(self, telegram_client: TelegramClient, database_client: SQLiteClient,
                 user_actioner: UserActioner, parser: SiteParser):
        self.telegram_client = telegram_client
        self.database_client = database_client
        self.user_actioner = user_actioner
        self.parser = parser
        self.setted_up = False

    def setup(self):
        self.database_client.create_conn()
        self.setted_up = True

    def shutdown(self):
        self.database_client.close_conn()

    def notify(self, notify_ids: list):
        for chat_id, user_id in notify_ids:
            res = self.telegram_client.post(method="sendMessage", params={
                "text": NOTIFY_MSG % str(date.today() + timedelta(days=TIME_DELTA)),
                "chat_id": chat_id})
            self.user_actioner.update_notify_date(user_id=user_id, updated_date=None)
            logger.info(res)

    def track(self, track_ids: list):
        for chat_id, user_id, track_data in track_ids:
            track_data = track_data.split()
            if self.parser.get_free_seats(track_data[0], track_data[1], track_data[2], track_data[3]):
                res = self.telegram_client.post(method="sendMessage", params={
                    "text": TRACK_MSG % (track_data[2], track_data[0], track_data[1], track_data[3]),
                    "chat_id": chat_id,
                    "parse_mode": 'markdown'})
                self.user_actioner.update_track_data(user_id=user_id, updated_data=None)
                logger.info(res)

    def execute_notify(self):
        if not self.setted_up:
            logger.error("Resources in worker.reminder has not been set up!")
            return
        logger.info('The execute_notify function is called')
        notify_ids = self.database_client.execute_select_command(self.GET_NOTIFY_DATE)
        if notify_ids:
            self.notify(notify_ids)

    def execute_track(self):
        if not self.setted_up:
            logger.error("Resources in worker.reminder has not been set up!")
            return
        logger.info('The execute_track function is called')
        track_ids = self.database_client.execute_select_command(self.GET_TRACK_DATA)
        if track_ids:
            self.track(track_ids)
