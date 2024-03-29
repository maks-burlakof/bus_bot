import datetime
import calendar
import typing
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


class Calendar:
    """
    Calendar data factory
    """

    def __init__(self, sep):
        self.__days = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
        self.__months = (
            "Январь ❄️",
            "Февраль 🌨",
            "Март 🌤",
            "Апрель ☀️",
            "Май 🏖",
            "Июнь 🌴",
            "Июль 🌞",
            "Август ⛱",
            "Сентябрь 🍁",
            "Октябрь 🍃",
            "Ноябрь 🌧",
            "Декабрь 🎄",
        )
        self.sep = sep

    def create_calendar(self, name: str = "calendar", year: int = None, month: int = None) -> InlineKeyboardMarkup:
        """
        Create a built-in inline keyboard with calendar

        :param name:
        :param year: Year to use in the calendar if you are not using the current year.
        :param month: Month to use in the calendar if you are not using the current month.
        :return: Returns an InlineKeyboardMarkup object with a calendar.
        """

        now_day = datetime.datetime.now()

        if year is None:
            year = now_day.year
        if month is None:
            month = now_day.month

        calendar_callback = CallbackData(name, "action", "year", "month", "day", sep=self.sep)
        data_ignore = calendar_callback.new("IGNORE", year, month, "!")
        data_months = calendar_callback.new("MONTHS", year, month, "!")

        keyboard = InlineKeyboardMarkup(row_width=7)

        keyboard.add(InlineKeyboardButton(
            self.__months[month - 1] + " " + str(year),
            callback_data=data_months,
            ))

        keyboard.add(*[
            InlineKeyboardButton(day, callback_data=data_ignore)
            for day in self.__days
        ])

        for week in calendar.monthcalendar(year, month):
            row = list()
            for day in week:
                if day == 0:
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                elif f"{now_day.day}.{now_day.month}.{now_day.year}" == f"{day}.{month}.{year}":
                    row.append(InlineKeyboardButton(f"{day}",
                                                    callback_data=calendar_callback.new("DAY", year, month, day)))
                elif datetime.datetime(year, month, day) < now_day:
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                else:
                    row.append(InlineKeyboardButton(str(day),
                                                    callback_data=calendar_callback.new("DAY", year, month, day)))
            keyboard.add(*row)

        if month == now_day.month:
            keyboard.add(InlineKeyboardButton("❌ Отменить",
                                              callback_data=calendar_callback.new("CANCEL", year, month, "!")),
                         InlineKeyboardButton("👉🏼",
                                              callback_data=calendar_callback.new("NEXT-MONTH", year, month, "!")))
        else:
            keyboard.add(InlineKeyboardButton("👈🏼",
                                              callback_data=calendar_callback.new("PREVIOUS-MONTH", year, month, "!")),
                         InlineKeyboardButton("❌ Отмена",
                                              callback_data=calendar_callback.new("CANCEL", year, month, "!")),
                         InlineKeyboardButton("👉🏼",
                                              callback_data=calendar_callback.new("NEXT-MONTH", year, month, "!")))
        return keyboard

    def create_months_calendar(self, name: str = "calendar", year: int = None) -> InlineKeyboardMarkup:
        """
        Creates a calendar with month selection

        :param name:
        :param year:
        :return:
        """

        if year is None:
            year = datetime.datetime.now().year

        calendar_callback = CallbackData(name, "action", "year", "month", "day", sep=self.sep)

        keyboard = InlineKeyboardMarkup()

        for i, month in enumerate(
            zip(self.__months[0::2], self.__months[1::2])
        ):
            keyboard.add(
                InlineKeyboardButton(
                    month[0],
                    callback_data=calendar_callback.new("MONTH", year, 2 * i + 1, "!"),
                ),
                InlineKeyboardButton(
                    month[1],
                    callback_data=calendar_callback.new(
                        "MONTH", year, (i + 1) * 2, "!"
                    ),
                ),
            )
        keyboard.add(InlineKeyboardButton(
            "❌ Отменить",
            callback_data=calendar_callback.new("CANCEL", year, 1, "!")
        ))

        return keyboard

    def calendar_query_handler(
        self,
        bot: TeleBot,
        call: CallbackQuery,
        name: str,
        action: str,
        year: int,
        month: int,
        day: int,
    ) -> None or datetime.datetime:
        """
        The method creates a new calendar if the forward or backward button is pressed
        This method should be called inside CallbackQueryHandler.


        :param bot: The object of the bot CallbackQueryHandler
        :param call: CallbackQueryHandler data
        :param day:
        :param month:
        :param year:
        :param action:
        :param name:
        :return: Returns a tuple
        """

        bot.answer_callback_query(call.id)
        current = datetime.datetime(int(year), int(month), 1)
        if action == "IGNORE":
            return False, None
        elif action == "DAY":
            bot.delete_message(
                chat_id=call.message.chat.id, message_id=call.message.message_id
            )
            return datetime.date(int(year), int(month), int(day))
        elif action == "PREVIOUS-MONTH":
            preview_month = current - datetime.timedelta(days=1)
            bot.edit_message_text(
                text=call.message.text,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=self.create_calendar(
                    name=name,
                    year=int(preview_month.year),
                    month=int(preview_month.month),
                ),
            )
            return None
        elif action == "NEXT-MONTH":
            next_month = current + datetime.timedelta(days=31)
            bot.edit_message_text(
                text=call.message.text,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=self.create_calendar(
                    name=name, year=int(next_month.year), month=int(next_month.month)
                ),
            )
            return None
        elif action == "MONTHS":
            bot.edit_message_text(
                text=call.message.text,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=self.create_months_calendar(name=name, year=current.year),
            )
            return None
        elif action == "MONTH":
            bot.edit_message_text(
                text=call.message.text,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=self.create_calendar(
                    name=name, year=int(year), month=int(month)
                ),
            )
            return None
        elif action == "CANCEL":
            return "CANCEL", None
        else:
            bot.delete_message(
                chat_id=call.message.chat.id, message_id=call.message.message_id
            )
            return None


class CallbackData:
    """
    Callback data factory
    """

    def __init__(self, prefix, *parts, sep=";"):
        if not isinstance(prefix, str):
            raise TypeError(
                f"Prefix must be instance of str not {type(prefix).__name__}"
            )
        if not prefix:
            raise ValueError("Prefix can't be empty")
        if sep in prefix:
            raise ValueError(f"Separator {sep!r} can't be used in prefix")
        if not parts:
            raise TypeError("Parts were not passed!")

        self.prefix = prefix
        self.sep = sep

        self._part_names = parts

    def new(self, *args, **kwargs) -> str:
        """
        Generate callback data

        :param args:
        :param kwargs:
        :return:
        """

        args = list(args)

        data = [self.prefix]

        for part in self._part_names:
            value = kwargs.pop(part, None)
            if value is None:
                if args:
                    value = args.pop(0)
                else:
                    raise ValueError(f"Value for {part!r} was not passed!")

            if value is not None and not isinstance(value, str):
                value = str(value)

            if not value:
                raise ValueError(f"Value for part {part!r} can't be empty!'")
            if self.sep in value:
                raise ValueError(
                    f"Symbol {self.sep!r} is defined as the separator and can't be used in parts' values"
                )

            data.append(value)

        if args or kwargs:
            raise TypeError("Too many arguments were passed!")

        callback_data = self.sep.join(data)
        if len(callback_data) > 64:
            raise ValueError("Resulted callback data is too long!")

        return callback_data

    def parse(self, callback_data: str) -> typing.Dict[str, str]:
        """
        Parse data from the callback data

        :param callback_data:
        :return:
        """

        prefix, *parts = callback_data.split(self.sep)

        if prefix != self.prefix:
            raise ValueError("Passed callback data can't be parsed with that prefix.")
        elif len(parts) != len(self._part_names):
            raise ValueError("Invalid parts count!")

        result = {"@": prefix}
        result.update(zip(self._part_names, parts))

        return result

    def filter(self, **config):
        """
        Generate filter

        :param config:
        :return:
        """

        print(config, self._part_names)
        for key in config.keys():
            if key not in self._part_names:
                return False

        return True
