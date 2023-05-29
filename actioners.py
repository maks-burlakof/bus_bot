import json
from datetime import date
from typing import Union

from clients import SQLiteClient


class UserActioner:
    def __init__(self, database_client: SQLiteClient):
        self.database_client = database_client

    def setup(self):
        self.database_client.create_conn()
        self._create_tables()

    def shutdown(self):
        self.database_client.close_conn()

    def _create_tables(self):
        CREATE_USERS_TABLE = """
                CREATE TABLE IF NOT EXISTS users (
                    "user_id" INTEGER PRIMARY KEY NOT NULL UNIQUE,
                    "username" TEXT,
                    "chat_id" INTEGER NOT NULL,
                    "is_active" BOOLEAN NOT NULL CHECK ("is_active" IN (0, 1)),
                    "level" INT NOT NULL CHECK ("level" IN (1, 2)),
                    "notify_data" JSON,
                    "track_data" JSON,
                    "parse_data" JSON
                );
            """
        CREATE_CITY_DATA_TABLE = """
                CREATE TABLE IF NOT EXISTS city_data (
                    "name" TEXT NOT NULL,
                    "key" TEXT NOT NULL
                );
            """
        CREATE_INVITE_CODES_TABLE = """
                CREATE TABLE IF NOT EXISTS invite_codes (
                    "code" TEXT NOT NULL
                );
            """
        self.database_client.execute_command(CREATE_USERS_TABLE, ())
        self.database_client.execute_command(CREATE_CITY_DATA_TABLE, ())
        self.database_client.execute_command(CREATE_INVITE_CODES_TABLE, ())

    @staticmethod
    def _get_json_data(raw_data) -> list:
        try:
            if isinstance(raw_data, tuple):
                data = json.loads(raw_data[0])
            elif isinstance(raw_data, list):
                data = json.loads(raw_data[0][0])
            elif isinstance(raw_data, str):
                data = json.loads(raw_data)
            assert isinstance(data, list)
        except (json.decoder.JSONDecodeError, TypeError, IndexError, AssertionError):
            data = []
        return data

    @staticmethod
    def _json_dump(data) -> str:
        return json.dumps(data, ensure_ascii=False)

    # USERS ~~~~~~~~

    def get_user(self, user_id: int):
        user = self.database_client.execute_select_command('SELECT user_id, username, chat_id, notify_data, track_data, parse_data FROM users WHERE user_id = %s;' % user_id)
        if user:
            user = [elem for elem in user[0]]

            notify_data = self._get_json_data(user[3])
            if notify_data and not notify_data[-1]['date']:
                notify_data.pop(-1)
            user[3] = notify_data

            track_data = self._get_json_data(user[4])
            if track_data:
                if not track_data[-1]['date'] or not track_data[-1]['from'] or not track_data[-1]['to'] or not track_data[-1]['time']:
                    track_data.pop(-1)
            user[4] = track_data

            parse_data = self._get_json_data(user[5])
            if parse_data:
                if not parse_data[-1]['date'] or not parse_data[-1]['from'] or not parse_data[-1]['to']:
                    parse_data.pop(-1)
            user[5] = parse_data
        else:
            user = []
        return user

    def get_all_users(self):
        return self.database_client.execute_select_command('SELECT user_id, username, chat_id, notify_data, track_data FROM users')

    def add_active_user(self, user_id: str, username: str, chat_id: int):
        empty_list = json.dumps([])
        self.database_client.execute_command('INSERT INTO users (user_id, username, chat_id, is_active, level, notify_data, track_data, parse_data) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', (user_id, username, chat_id, 1, 1, empty_list, empty_list, empty_list))

    def is_user_active(self, user_id) -> bool:
        result_list = self.database_client.execute_select_command('SELECT is_active FROM users WHERE user_id = {};'.format(user_id))
        if result_list:
            return True if result_list[0][0] == 1 else False
        else:
            return False

    def make_user_active(self, user_id: int):
        self.database_client.execute_command('UPDATE users SET is_active = 1 WHERE user_id = ?', (user_id,))

    def make_user_inactive(self, user_id: int):
        self.database_client.execute_command('UPDATE users SET is_active = 0 WHERE user_id = ?', (user_id,))

    # INVITE CODES ~~~~~~~~

    def get_invite_codes(self):
        return self.database_client.execute_select_command('SELECT code FROM invite_codes')

    def add_invite_code(self, code: str):
        self.database_client.execute_command('INSERT INTO invite_codes (code) VALUES (?);', (code,))

    def remove_invite_code(self, code: str):
        self.database_client.execute_command('DELETE FROM invite_codes WHERE code = ?;', (code,))

    # CITY DATA ~~~~~~~~

    def get_city_data(self):
        data = self.database_client.execute_select_command('SELECT name, key FROM city_data')
        return {name: key for name, key in data}

    # NOTIFY ~~~~~~~~

    def add_notify_date(self, user_id: int):
        json_template = {
            'date': ''
        }
        raw_data = self.database_client.execute_select_command('SELECT notify_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)

        if data and not data[-1]['date']:
            data.pop(-1)  # delete last unfinished addition

        data.append(json_template)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET notify_data = ? WHERE user_id = ?;', (completed_data, user_id))

    def update_last_notify_date(self, user_id: int, key: str, value: str) -> bool:
        """
        Update last notify record.
        :return: Record creation result.
        """
        raw_data = self.database_client.execute_select_command('SELECT notify_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        is_unique = value not in [dict_record['date'] for dict_record in data]
        if is_unique:
            data[-1][key] = value
        else:
            data.pop(-1)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET notify_data = ? WHERE user_id = ?;', (completed_data, user_id))
        return is_unique

    def remove_notify_date(self, user_id: int, index: int):
        raw_data = self.database_client.execute_select_command('SELECT notify_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        data.pop(index)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET notify_data = ? WHERE user_id = ?;', (completed_data, user_id))

    # TRACK ~~~~~~~~

    def add_track_date(self, user_id: int):
        json_template = {
            'date': '',
            'from': '',
            'to': '',
            'time': '',
            'passed': '',
            'is_active': ''
        }
        raw_data = self.database_client.execute_select_command('SELECT track_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)

        if data:
            if not data[-1]['date'] or not data[-1]['from'] or not data[-1]['to'] or not data[-1]['time']:
                data.pop(-1)  # delete last unfinished addition

        data.append(json_template)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET track_data = ? WHERE user_id = ?;', (completed_data, user_id))

    def update_last_track_date(self, user_id: int, key: str, value: str):
        """
        Update last track record.
        :return: Record creation result.
        """
        raw_data = self.database_client.execute_select_command('SELECT track_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        is_unique = True
        if key == 'time':  # the last step in a new track record creation
            for dict_record in data[:-1]:
                if data[-1]['date'] == dict_record['date'] and data[-1]['from'] == dict_record['from'] and \
                        data[-1]['to'] == dict_record['to'] and value == dict_record['time']:
                    is_unique = False
                    break
            if is_unique:
                data[-1][key] = value
            else:
                data.pop(-1)
        else:
            data[-1][key] = value
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET track_data = ? WHERE user_id = ?;', (completed_data, user_id))
        return is_unique

    def get_last_track_date(self, user_id: int) -> dict:
        """
        :return: The last uncompleted track data record.
        """
        raw_data = self.database_client.execute_select_command('SELECT track_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        last_record = data[-1]
        return last_record

    def remove_track_date(self, user_id: int, index: int):
        raw_data = self.database_client.execute_select_command('SELECT track_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        data.pop(index)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET track_data = ? WHERE user_id = ?;', (completed_data, user_id))

    def update_track_time_passed(self, user_id: int, updated_delta: Union[int, None]):  # TODO: deprecated
        if updated_delta == -1:
            self.database_client.execute_command('UPDATE users SET track_time_passed = track_time_passed + ? WHERE user_id = ?;', (1, user_id))
        else:
            self.database_client.execute_command('UPDATE users SET track_time_passed = ? WHERE user_id = ?;', (updated_delta, user_id))

    def same_track_data_count(self, track_data: str) -> int:  # TODO: rewrite
        same_count = self.database_client.execute_select_command('SELECT COUNT(*) FROM users WHERE track_data = "%s";' % track_data)
        return int(same_count[0][0]) - 1

    # PARSE ~~~~~~~~

    def add_parse_date(self, user_id: int):
        json_template = {
            'date': '',
            'from': '',
            'to': ''
        }
        raw_data = self.database_client.execute_select_command('SELECT parse_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)

        if data:
            if not data[-1]['date'] or not data[-1]['from'] or not data[-1]['to']:
                data.pop(-1)  # delete last unfinished addition

        data.append(json_template)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET parse_data = ? WHERE user_id = ?;', (completed_data, user_id))

    def get_last_parse_data(self, user_id: int) -> dict:
        """
        :return: The last uncompleted parse data record.
        """
        raw_data = self.database_client.execute_select_command('SELECT parse_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        last_record = data[-1]
        return last_record

    def update_last_parse_data(self, user_id: int, key: str, value: str):
        """
        Update the last uncompleted parse record.
        """
        raw_data = self.database_client.execute_select_command('SELECT parse_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        data[-1][key] = value
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET parse_data = ? WHERE user_id = ?;', (completed_data, user_id))

    def remove_parse_date(self, user_id: int, index: int):
        raw_data = self.database_client.execute_select_command('SELECT parse_data FROM users WHERE user_id = %s;' % user_id)
        data = self._get_json_data(raw_data)
        data.pop(index)
        completed_data = self._json_dump(data)
        self.database_client.execute_command('UPDATE users SET parse_data = ? WHERE user_id = ?;', (completed_data, user_id))
