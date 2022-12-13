START_NEW_USER_MSG = 'Привет, %s 👋!\n' \
    'Я бот, который будет помогать тебе заказывать маршрутки с сайта _route.by_. Надеюсь я помогу тебе поскорее ' \
    'уехать домой и забыть на пару дней о контрольных, зачетах и экзаменах, которые ждут тебя в университете 🤓. ' \
    'Просто открой меню и посмотри, что я могу для тебя сделать.'

START_FEATURES_MSG = '*А вот и список того, что я уже умею:*\n' \
    '- получение уведомлений о доступности выбранных рейсов\n' \
    '- получение информации со страницы заказа на сайте route.by\n' \
    '- получение уведомлений о появлении свободных мест на выбранный рейс\n' \
    '- настройка уникальных параметров:\n' \
    '     - частоты опроса с сайта\n' \
    '- отправка сообщения администратору\n' \

START_OLD_USER_MSG = 'О, ты тоже тут? Просто открой меню и посмотри, что я могу для тебя сделать.'

NOTIFY_INPUT_MSG = 'Выбери дату и я сразу напомню, когда рейсы будут доступны для заказа.'

NOTIFY_MSG = 'Появились рейсы на %s! Не забудь заказать!'

LOADING_MSGS = [
    'Загружаю данные...',
    'Загрузка данных...',
    'Отправляю запрос...',
    'Обрабатываю запрос...',
    'Секундочку...',
    'Загружаюсь...',
]

CANCEL_MSGS = [
    'Операция отменена.',
]

NO_BUSES_MSGS = [
    'Упс! Что-то я не нашел рейсов на этот день.',
    'Не могу найти рейсы на этот день 🤷‍♂️.',
    'Ой, произошла ошибка. Что-то я не нашел рейсов на этот день.',
]

PARSE_INPUT_MSG = 'Отправь мне через пробел город отправления, город прибытия и дату в формате ‘2023-01-13’. '

TRACK_INPUT_MSG = 'Выбери дату, город отправления и прибытия, время отправления рейса. ' \
                  'Я сразу скажу тебе, когда появится свободное местечко!'

TRACK_MSG = 'Появились свободные места на рейс %s \n' \
            '%s - %s в %s\n' \
            'Успей заказать!'

NOTIFY_TRACK_SET_MSGS = [
    'Отлично! Обещаю, что буду смотреть очень внимательно 🤠!',
    'Отлично! Я буду следить очень внимательно 🕵️‍♂️!',
    'Класс! Я буду очень внимательным!',
    'Отлично! Ты можешь рассчитывать на меня.',
    'Приступаю к работе!',
]

EXTRA_MSG = '<b>Здесь спрятались мои дополнительные возможности:</b>\n' \
            '/description - Описание проекта\n'\
            '/feedback - Отправка сообщения администратору\n'

EXTRA_ADMIN_MSG = '/announcement_text - Объявление (текстовое) для пользователей\n' \
                  '/announcement_auto - Объявление (с форматированием) для пользователей\n'

DESCRIPTION_MSG = '[Смотреть README.md на GitHub](https://github.com/' \
                  'maks-burlakof/bus_bot/blob/main/README.md)'

FEEDBACK_MSG = '✍️ Вижу, ты захотел отправить сообщение администратору. Что ж, пиши:'

FEEDBACK_SUBMIT_MSG = 'Готово! Я уже отправил весточку.'

FEEDBACK_TO_ADMIN_MSG = 'Пользователь @%s отправил сообщение:\n%s'

ANNOUNCEMENT_TEXT = '*🔔 Объявление:*\n'

ANNOUNCEMENT_TEXT_INPUT_MSG = 'Отправь текст объявления, которое будет отправлено всем пользователям'

ANNOUNCEMENT_TEXT_CONFIRMATION_MSG = 'Вы уверены, что хотите отправить это объявление всем пользователям?\nДа/Нет'

ANNOUNCEMENT_TEXT_SENT_MSG = 'Объявление отправлено всем участникам'

NO_RIGHTS_MSG = 'Извини, но ты не можешь использовать эту команду 😢...'

ORDINARY_TEXT_MSGS = [
    'Бип-буп. На такую команду я не запрограммирован.',
    'Выбери, пожалуйста, команду из меню 😅',
    'Что-то я не понимаю о чем ты говоришь... Посмотри в меню, что я умею.',
]

FEATURE_NOT_ADDED = [
    'Прости, но эту функцию пока не добавили. Посмотри в меню, что я умею.',
    'Извини, эта функция еще в разработке. Посмотри в меню, что я умею.'
]

SECRET_MSG = '||по пиву сегодня?||'
