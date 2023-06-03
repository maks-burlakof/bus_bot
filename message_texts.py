def plural(value: int, variants: str) -> str:
    variants = variants.split(",")
    value = abs(int(value))
    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return variants[variant]


START_NEW_USER_MSG = 'Привет, %s 👋!\n' \
    'Я бот, который будет помогать тебе заказывать маршрутки с сайта _route.by_. Надеюсь я помогу тебе поскорее ' \
    'уехать домой и забыть на пару дней о контрольных, зачетах и экзаменах, которые ждут тебя в университете 🤓. ' \
    'Просто открой меню и посмотри, что я могу для тебя сделать.'

START_FEATURES_MSG = '*А вот и список того, что я уже умею:*\n' \
    '- искать маршрутки на сайте route.by\n' \
    '- напоминать, когда маршрутки появятся в расписании\n' \
    '- уведомлять, когда появляются свободные места на выбранные маршрутки\n'

USER_NOT_ALLOWED_MSG = [
    'Упс 😲, кажется ты не можешь этого сделать.\n',
    'Хмм 🤔 что-то я не нашел тебя в своей базе данных.\n',
    'О, привет 👋! Ты наверное новенький, сначала надо зарегистрироваться.\n',
]

USER_NOT_ALLOWED_BASE_MSG = 'Если у тебя есть пригласительный код, используй /register.\n' \
                            'А написать админу можно здесь - /feedback.'

REGISTER_MSG = '📧 Отправь свой пригласительный код'

REGISTER_EXISTS_MSG = 'Что-то мне подсказывает, что ты уже зарегистрирован ☺️\n' \
                      'Я готов выполнить любую твою просьбу!'

REGISTER_CODE_INCORRECT_MSG = 'Код неверный! 😕'

REGISTER_CODE_CORRECT_MSG = 'Код верный! Поздравляю с успешной регистрацией! 🎊'

INVITE_CODES_LIST_MSG = '*Доступные пригласительные коды:*\n'

INVITE_CODES_CREATED_MSG = 'Новые 5 пригласительных кодов были сгенерированы и добавлены.'

NOTIFY_EXISTS_MSG = '*Отслеживаемые даты:*'

NOTIFY_RESET_EXISTS_MSGS = [
    'Хорошо, я перестал отслеживать эту дату.',
    'Окей, теперь я не отслеживаю эту дату.',
]

TRACK_EXISTS_MSG = '*Отслеживаемые*\n*маршрутки:*'

NOTIFY_TEMPLATE_MSG = '📆 %s'

TRACK_BUS_TEMPLATE_MSG = '%s\n%s 👉🏼 %s\n🕓 %s'

TRACK_RESET_EXISTS_MSGS = [
    'Хорошо, я перестал отслеживать эту маршрутку.',
    'Окей, теперь я не отслеживаю эту маршрутку.',
    'Ладно, убрал эту штуку из базы данных.',
    'Сделано! Отменил эту маршрутку.',
    'Минус один, юхуу!',
    'Окей, забыли про это.',
]

NOTIFY_INPUT_MSG = 'Выбери дату и я сразу напомню, когда рейсы будут доступны для заказа.'

NOTIFY_MSG = '🔔 *Появились рейсы!* \n📆 %s\nНе забудь заказать!'

LOADING_MSGS = [
    'Загружаю данные...',
    'Загрузка данных...',
    'Отправляю запрос на Марс...',
    'Ищу жизнь на Марсе...',
    'Загрузочка...',
    'Выполняю запрос...',
    'Обрабатываю запрос...',
    'Секундочку...',
    'Загружаюсь...',
    'Получаю данные...',
    'Загрузка информации...',
    'Идет загрузка данных...',
    'Подожди, пожалуйста...',
    'Данные готовятся...',
    'Загрузка контента...',
    'Подгружаюсь бип буп...',
    'Ща все организую...',
    'Пытаюсь узнать ну как там с деньгами...',
    'Loading. Please stand by...',
]

CANCEL_MSGS = [
    'Операция отменена',
    'Отменено',
    'Операция отклонена',
    'Ладно, забыли',
    'Отбой, отмена',
]

NO_BUSES_MSGS = [
    'Упс 😞... Что-то я не нашел рейсов на этот день',
    'Не могу найти рейсы на этот день 🤷‍♂️',
    'Кажется, я не нашел рейсов на этот день 🙈',
]

PARSE_INPUT_MSG = 'Выбери дату:'

RECORD_NOT_EXISTS_MSGS = [
    'Не могу найти такую запись 🤷🏼‍♂️\nДавай попробуем еще раз.',
    'Чето не так. Не могу найти это в своей базе данных 🤷🏼‍♂️',
    'Ничего не понимаю, какая-то белеберда. Давай попробуем еще раз ☺️',
    'ERROR 404 KFP15-PIVO-NOT-FOUND-FJ56.\nДа, явно произошла какая-то ошибка. Давай попробуем выполнить это действие еще раз.'
]

# parse_input_route не должен быть равен track_input_route
PARSE_INPUT_ROUTE_MSG = 'Укажи маршрут:'

SELECTED_DATE_MSG = '\n📆 %s'

SELECTED_ROUTE_MSG = '\n%s 👉🏼 %s'

PARSE_RESPONSE_HEADER_MSG = '*%s 👉🏼 %s*\n*%s*\n'

TRACK_INPUT_DATE_MSG = 'Выбери дату:\n' \
                       'Я сразу же напишу тебе, когда появится свободное местечко!'

TRACK_INPUT_ROUTE_MSG = 'Укажи маршрут рейса:'

TRACK_INPUT_DEPARTURE_TIME_MSG = '🕓 Выбери время отправления рейса:'

TRACK_MSG = '🔔 *Появились свободные места!*\n📆 %s\n%s 👉🏼 %s\n🕓 %s\n' \
            'Успей заказать!'

TRACK_FREE_PLACES_EXISTS_MSGS = [
    'На этот рейс уже есть свободные места. Можешь бронировать!',
]

TRACK_RECORD_EXIST_MSGS = [
    'Кажется, ты уже отслеживаешь эту маршрутку, взгляни 🙈',
]

NOTIFY_BUS_EXISTS_MSGS = [
    'Хмм... Рейсы на эту дату уже есть в расписании. Можешь бронировать места!',
]

NOTIFY_RECORD_EXIST_MSGS = [
    'Похоже, ты уже отслеживаешь эту дату.',
]

NOTIFY_TRACK_SET_MSGS = [
    'Отлично! Обещаю, что буду смотреть очень внимательно 🤠!',
    'Записал тебя в свою тетрадочку. Пока только карандашом.',
    'Отлично! Я буду следить очень внимательно! 🕵️‍♂️',
    'Окей, буду очень внимательным!',
    'Отлично! Ты можешь рассчитывать на меня.',
    'Не знаю даже... Анекдоты что ли начать отправлять?',
    'Ну вот, теперь в базе данных стало на одну запись больше',
    'Окей, начинаю отправлять реквесты, всё для тебя, зайка ❤️',
    'Ладно, стартуем!',
    'The show must go on!',
    'Приступаю к работе!',
    'Успешно! *звук ржавых шестеренок*',
    'Ок. просто ок.',
    'HTTP response 200 OK',
]


def notify_track_limit_exceeded_msg(max_buses: int):
    return 'Достигнут лимит на добавление 😞\nТы можешь отслеживать только {} {} и {}.'.format(
        max_buses, plural(max_buses, "маршрутка,маршрутки,маршруток"), plural(max_buses, "дата,даты,дат")
    )


EXTRA_MSG = '<b>Здесь спрятались мои дополнительные возможности:</b>\n' \
            '/description - Описание проекта\n'\
            '/faq - Часто задаваемые вопросы\n'\
            '/feedback - Обратная связь\n'

EXTRA_ADMIN_MSG = '👨‍👩‍👦‍👦 <b>Пользователи:</b>\n' \
                  '/database - Просмотреть БД\n' \
                  '/users - Список зарегистрированных юзеров\n' \
                  '/ban - Убрать юзера из списка разрешенных\n' \
                  '🔔 <b>Объявления:</b>\n' \
                  '/announcement_text - Объявление (текстовое)\n' \
                  '/announcement_auto - Объявление (с форматированием)\n' \
                  '📃 <b>Логи:</b>\n' \
                  '/logs - Отправить файл логов\n' \
                  '/clear_logs - Очистить файл логов\n' \
                  '🔐 <b>Пригласительные коды:</b>\n' \
                  '/invite_codes - Просмотреть список пригласительных кодов\n' \
                  '/invite_codes_create - Создать новые пригласительные коды\n' \
                  '🤖 <b>Бот:</b>\n' \
                  '/exit - Выключение бота\n'

DESCRIPTION_MSG = 'Текущая версия: v2.0\n' \
                  '[Смотреть README.md на GitHub](https://github.com/' \
                  'maks-burlakof/bus_bot/blob/main/README.md)'


def statistics_msg(users_num: int, notify_num: int, track_num: int, pivo_num):
    return '*Статистика:*\n' +\
        '👨‍🦳 {} {}\n'.format(users_num, plural(users_num, 'пользователь,пользователя,пользователей')) +\
        '🔸 {} {} мониторится\n'.format(notify_num, plural(notify_num, 'дата,даты,дат')) +\
        '🔹 {} {} отслеживается\n'.format(track_num, plural(track_num, 'маршрутка,маршрутки,маршруток')) +\
        '🍺 {} {} остывает в холодильнике'.format(pivo_num, plural(pivo_num, 'пиво,пива,пив'))


FAQ_MSG = '*Часто задаваемые вопросы:*\n\n' \
          '*Почему бот не работает?*\n' \
          'Я не знаю 🤷🏼‍♂️. Возможно сейчас идут технические работы, а возможно что-то поломалось\n\n' \
          '*Почему так долго загружаются данные с сайта?*\n' \
          'Это может быть связано сразу с несколькими причинами. Так как бот напрямую обращается к сайту маршруток ' \
          'без использования API, время загрузки зависит от скорости серверов маршрутчика, а также от моих серверов, ' \
          'на которых работает бот. Легко узнать что вызывает проблему - если в официальном приложении данные ' \
          'загружаются быстро, значит проблема на моей стороне.\n\n' \
          '*Почему бот не отправляет уведомление о появлении свободных мест?*\n' \
          'Если ты уверен, что место действительно было, а бот не отправил уведомление - сообщи мне об этом. ' \
          'Возможно что-то поломалось...\n\n' \

FEEDBACK_MSG = '✍️ Окей, а теперь придумай что написать.'

FEEDBACK_SUBMIT_MSG = 'Готово! Я уже отправил весточку.'

FEEDBACK_CONFIRMATION_MSG = 'Отлично, осталось последнее действие. Ты знаешь, что делать😎\n' \
                            'Кстати внизу предпросмотр твоего сообщения 👇'

FEEDBACK_TO_ADMIN_MSG = '🔔 %s намяукал:\n%s'

ANNOUNCEMENT_TEXT_MSG = '*🔔 Объявление:*\n%s'

ANNOUNCEMENT_TEXT_INPUT_MSG = 'Отправь текст объявления, которое будет отправлено всем пользователям'

ANNOUNCEMENT_TEXT_CONFIRMATION_MSG = 'Предпросмотр объявления.\n' \
                                     'Чтобы отправить объявление всем пользователям отправь `Отправить`'

ANNOUNCEMENT_TEXT_SENT_MSG = 'Объявление отправлено всем пользователям'

USER_LIST_MSG = '<b>Зарегистрированные пользователи:</b>\n'

BAN_USER_MSG = 'Отправьте *id пользователя*, которого хотите заблокировать\.\n' \
               'Для отмены операции отправьте `Отменить`\.'

BAN_USER_CONFIRMATION_MSG = 'Нашел этого человечка %s! В бан его!'

DATABASE_LIST_MSG = '<b>Содержимое базы данных:</b>\n'

EXIT_CONFIRMATION_MSG = '*Внимание!*\nЭта операция *остановит работу бота на сервере*. ' \
                        'Возможно, вам стоит сначала оповестить пользователей о временном ' \
                        'прекращении работы бота. Для продолжения отправьте `Выключение`:'

EXIT_MSG = 'Работа бота завершена по вашей инициативе.'

NO_RIGHTS_MSG = 'Извини, но ты не можешь использовать эту команду 😢...'

INT_INPUT_INCORRECT = 'Ой-ой, действие не выполнено. Ожидается целое число, а тут ерунда какая-то. Теперь все заново 😘'

ORDINARY_TEXT_MSGS = [
    'Бип-буп. На такую команду я не запрограммирован.',
    'Выбери, пожалуйста, команду из меню 😅',
    'Что-то я не понимаю о чем ты говоришь... Посмотри в меню, что я умею.',
    'ERROR 404 KFPEJ43JIF-PIVO-NOT-FOUND.\nНу а вообще, такой команды не существует 🫣',
]

FEATURE_NOT_ADDED_MSGS = [
    'Прости, но эту функцию пока не добавили. Посмотри в меню, что я умею.',
    'Извини, эта функция еще в разработке. Посмотри в меню, что я умею.'
]

SECRET_MSG = '||по пиву сегодня?||'
