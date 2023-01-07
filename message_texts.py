START_NEW_USER_MSG = 'Привет, %s 👋!\n' \
    'Я бот, который будет помогать тебе заказывать маршрутки с сайта _route.by_. Надеюсь я помогу тебе поскорее ' \
    'уехать домой и забыть на пару дней о контрольных, зачетах и экзаменах, которые ждут тебя в университете 🤓. ' \
    'Просто открой меню и посмотри, что я могу для тебя сделать.'

START_FEATURES_MSG = '*А вот и список того, что я уже умею:*\n' \
    '- отправлять уведомления о доступности выбранных рейсов\n' \
    '- отправлять уведомления о появлении свободных мест на выбранный рейс\n' \
    '- получать информацию о рейсах с сайта route.by\n' \
    '- отправлять сообщения администратору\n' \

START_OLD_USER_MSG = 'О, ты тоже тут? Просто открой меню и посмотри, что я могу для тебя сделать.'

USER_NOT_ALLOWED_MSG = [
    'Упс 🤔, кажется у тебя нет прав на использование этой команды.\n'
    'Если у тебя есть пригласительный код, используй /register\n'
    'Также ты всегда можешь связаться с администратором /feedback, если считаешь что произошла ошибка.'
]

REGISTER_MSG = '📧 Отправь свой пригласительный код'

REGISTER_CODE_INCORRECT_MSG = 'Код неверный! 😕'

REGISTER_CODE_CORRECT_MSG = 'Код верный! Поздравляю с успешной регистрацией! 🎊'

INVITE_CODES_CREATED_MSG = 'Новые 5 пригласительных кодов были сгенерированы и добавлены.'

# Все _exists не должны быть равны и на конце должно быть \n%s
NOTIFY_EXISTS_MSG = 'Отслеживаемая дата:\n%s'

NOTIFY_RESET_EXISTS_MSGS = [
    'Хорошо, я перестал отслеживать рейсы на эту дату',
    'Окей, теперь я не отслеживаю рейсы на эту дату',
]

TRACK_EXISTS_MSG = 'Текущий отслеживаемый рейс:\n%s\n%s 👉🏼 %s\n🕓 %s'

TRACK_RESET_EXISTS_MSGS = [
    'Хорошо, я перестал отслеживать этот рейс',
    'Окей, теперь я не отслеживаю этот рейс',
]

NOTIFY_INPUT_MSG = 'Выбери дату и я сразу напомню, когда рейсы будут доступны для заказа.'

NOTIFY_MSG = '🔔 *Появились рейсы!* \n📆 %s\nНе забудь заказать!'

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

PARSE_INPUT_MSG = 'Выбери дату:'

# parse_input_route не должен быть равен track_input_route
PARSE_INPUT_ROUTE_MSG = 'Укажи маршрут:'

PARSE_RESPONSE_HEADER_MSG = '*%s 👉🏼 %s*\n*%s*\n'

TRACK_INPUT_DATE_MSG = 'Выбери дату:\n' \
                  'Я сразу скажу тебе, когда появится свободное местечко!'

TRACK_INPUT_ROUTE_MSG = 'Укажи маршрут рейса:'

TRACK_INPUT_DEPARTURE_TIME_MSG = '🕓 Выбери время отправления рейса:'

TRACK_MSG = '🔔 *Появились свободные места!*\n📆 %s\n%s 👉🏼 %s\n🕓 %s\n' \
            'Успей заказать!'

TRACK_FREE_PLACES_EXISTS_MSGS = [
    'На этот рейс уже есть свободные места. Можешь бронировать!',
]

NOTIFY_BUS_EXISTS_MSGS = [
    'Хмм... Рейсы на эту дату уже есть в расписании. Можешь бронировать места!',
]

NOTIFY_TRACK_SET_MSGS = [
    'Отлично! Обещаю, что буду смотреть очень внимательно 🤠!',
    'Отлично! Я буду следить очень внимательно 🕵️‍♂️!',
    'Класс! Я буду очень внимательным!',
    'Отлично! Ты можешь рассчитывать на меня.',
    'Приступаю к работе!',
]

URL_TO_SITE_MSGS = [
    '👉🏼 [Ссылка на сайт для покупки](%s)'
]

EXTRA_MSG = '<b>Здесь спрятались мои дополнительные возможности:</b>\n' \
            '/description - Описание проекта\n'\
            '/faq - Часто задаваемые вопросы\n'\
            '/feedback - Отправить сообщение администратору\n'

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

DESCRIPTION_MSG = 'Текущая версия: v1.1\n' \
                  '[Смотреть README.md на GitHub](https://github.com/' \
                  'maks-burlakof/bus_bot/blob/main/README.md)'

STATISTICS_MSG = '*Статистика:*\n' \
                 'Пользователей зарегистрировано: *%d*\n' \
                 '🔸 Ждут появления рейсов: %d\n' \
                 '🔹 Рейсов отслеживается: %d\n' \

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

FEEDBACK_MSG = '✍️ Вижу, ты захотел отправить сообщение администратору. Что ж, пиши:'

FEEDBACK_SUBMIT_MSG = 'Готово! Я уже отправил весточку.'

FEEDBACK_CONFIRMATION_MSG = 'Чтобы подтвердить отправку сообщения, введи `Отправить`\nПредпросмотр:'

FEEDBACK_TO_ADMIN_MSG = '🔔 Пользователь @%s отправил сообщение:\n%s'

ANNOUNCEMENT_TEXT_MSG = '*🔔 Объявление:*\n%s'

ANNOUNCEMENT_TEXT_INPUT_MSG = 'Отправь текст объявления, которое будет отправлено всем пользователям'

ANNOUNCEMENT_TEXT_CONFIRMATION_MSG = 'Предпросмотр объявления.\n' \
                                     'Чтобы отправить объявление всем пользователям отправь `Отправить`'

ANNOUNCEMENT_TEXT_SENT_MSG = 'Объявление отправлено всем пользователям'

USER_LIST_MSG = '<b>Список всех зарегистрированных пользователей:</b>\n'

BAN_USER_MSG = 'Отправьте username (без @) пользователя, которого хотите заблокировать\n' \
           'Для отмены операции отправьте `Отменить`'

BAN_USER_CONFIRMATION_MSG = 'Операция выполнена. Если пользователь с таким именем существовал - он был забанен'

DATABASE_LIST_MSG = '<b>Содержимое базы данных:</b>\n'

EXIT_CONFIRMATION_MSG = '*Внимание!*\nЭта операция *остановит работу бота на сервере*. ' \
                        'Возможно, вам стоит сначала оповестить пользователей о временном ' \
                        'прекращении работы бота. Для продолжения отправьте `Выключение`:'

EXIT_MSG = 'Работа бота завершена по вашей инициативе.'

NO_RIGHTS_MSG = 'Извини, но ты не можешь использовать эту команду 😢...'

ORDINARY_TEXT_MSGS = [
    'Бип-буп. На такую команду я не запрограммирован.',
    'Выбери, пожалуйста, команду из меню 😅',
    'Что-то я не понимаю о чем ты говоришь... Посмотри в меню, что я умею.',
]

FEATURE_NOT_ADDED_MSGS = [
    'Прости, но эту функцию пока не добавили. Посмотри в меню, что я умею.',
    'Извини, эта функция еще в разработке. Посмотри в меню, что я умею.'
]

SECRET_MSG = '||по пиву сегодня?||'
